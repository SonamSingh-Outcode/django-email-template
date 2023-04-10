import logging
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.commons.utils.email import email_sender
from app.commons.utils.others import get_http_protocol
from app.commons.utils.token import generate_token
from config import settings

User = get_user_model()

logger = logging.getLogger(__name__)


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user_data = {
            "id": getattr(self.user, 'id', None),
            "email": getattr(self.user, 'email', None),
            "first_name": getattr(self.user, 'first_name', None),
            "middle_name": getattr(self.user, 'middle_name', None),
            "last_name": getattr(self.user, 'last_name', None)
        }
        attrs['user'] = user_data
        return attrs


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)

    def send_email_forget_password(self, user=None, email=None):
        if user:
            email = user.email
        else:
            email = self.validated_data.get('email') or email
            user = User.objects.get(email=email)
            if not user:
                return Response({"message": "If email exists with this tenant, reset e-mail will be sent."})

        uid, token = generate_token(user)

        context = {
            'email': email,
            'uid': uid,
            'token': token,
            'first_name': user.first_name,
            'reset_url': f'{get_http_protocol()}://{settings.FRONTEND_DOMAIN}/password/reset/{uid}/{token}'
        }

        email_sender(
            template='email/reset-password.html',
            context=context,
            subject="Reset your password",
            recipient_list=[email]
        )
        logger.info(f"Reset password email is send for user_id {user.id}")


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    def validate(self, data):
        if not data['new_password'] == data['confirm_password']:
            raise serializers.ValidationError("Passwords didn't match.")

        import re
        if not re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&()*_+=\\<>?,./-]).{6,}$",
                        data['new_password']):
            raise serializers.ValidationError(
                "Password must contain at least 6 characters with one number and one special character.")

        return data
