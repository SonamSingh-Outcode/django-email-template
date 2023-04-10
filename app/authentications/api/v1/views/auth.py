import logging
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError, PermissionDenied, NotFound
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView)

from app.authentications.api.v1.serializers import LoginSerializer, ResetPasswordSerializer, EmailSerializer
from app.commons.utils.browser import get_browser_detail
from app.commons.utils.email import email_sender
from app.commons.utils.token import verify_token

User = get_user_model()
logger = logging.getLogger(__name__)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        if not User.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'No active account found with the given credentials'},
                            status=HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = User.objects.get(id=serializer.validated_data['user']['id'])
        user.last_login = timezone.now()
        user.save()

        return Response(serializer.validated_data, status=HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except TokenError:
                raise PermissionDenied(
                    {'error': "`refresh` token not provided or token expired or you don't have permission."})
        else:
            raise ValidationError({'error': '`refresh` token is required.'})

        return Response({'detail': 'Successfully logged out.'})


class PasswordChangeView(CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        old_password = request.data.get('old_password')
        user = request.user
        if not old_password:
            raise ValidationError({'error': '`old_password` is required.'})

        if request.user.check_password(old_password) is False:
            raise ValidationError({'error': "`old_password` didn't match, try resetting you password."})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data.get('new_password'))
        request.user.save()
        try:
            email_sender(template='email/reset-password-success.html',
                         context={'first_name': user.first_name, **get_browser_detail(request)},
                         subject="Password Changed Successfully", recipient_list=[user.email])
        except Exception as error:
            logger.error(
                f'Error while sending password change email notification for user_id {user.id} \n{error}\n'
            )
        return Response({'success': 'Password has been changed with the new password.'})


class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email_serializer = EmailSerializer(data=request.data, context={'request': request})
        email_serializer.is_valid(raise_exception=True)
        email_serializer.send_email_forget_password()
        return Response({'message': 'If email account with this email, reset link will be sent.'})


class PasswordResetTokenVerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        uid = request.data.get('uid')
        if not (token and uid):
            raise ValidationError({'error': '`uid` or `token` is not provided'})
        user_id = force_str(urlsafe_base64_decode(uid))
        try:
            user = User.objects.get(pk=user_id)
            if verify_token(user, token):
                return Response()
            raise exceptions.ValidationError({'error': 'The link has already expired.'})
        except ObjectDoesNotExist:
            raise exceptions.ValidationError({'error': 'Token invalid or expired'})


class PasswordResetConfirmView(APIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        data = request.data
        token = data.get('token')
        uid = data.get('uid')
        if not (token and uid):
            raise ValidationError({'error': '`uid` or `token` is not provided'})
        user_id = force_str(urlsafe_base64_decode(uid))
        try:
            user = User.objects.get(pk=user_id)
            if verify_token(user, token):
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                user.set_password(serializer.validated_data.get('new_password'))
                user.save()
                logger.info(f"Password forgot and changed by user_id {user_id}")
                try:
                    email_sender(template='email/reset-password-success.html',
                                 context={'first_name': user.first_name, **get_browser_detail(request)},
                                 subject="Password Changed Successfully", recipient_list=[user.email])
                except Exception as error:
                    logger.error(
                        f'Error while sending password change email notification for user_id {user.id} \n{error}\n'
                    )
                return Response({'success': 'Password has been reset with the new password.'})
            logger.error(
                f"The link has expired when resetting password by user_id {user_id}")
            raise exceptions.ValidationError({'error': 'The link has already expired.'})
        except ObjectDoesNotExist:
            raise exceptions.ValidationError({'error': 'Token invalid or expired'})
