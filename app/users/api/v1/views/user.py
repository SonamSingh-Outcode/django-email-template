import logging
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

from app.commons.pagination import BasePageNumberPagination
from app.commons.viewsets import ListRetrieveUpdateDestroySetMixin
from ..serializers import UserSerializer
from ....constants import ADMIN
from ....models import User

logger = logging.getLogger(__name__)


class UsersViewSet(ListRetrieveUpdateDestroySetMixin):
    queryset = User.objects.filter(deleted_at__isnull=True).order_by('updated_at')
    serializer_class = UserSerializer
    pagination_class = BasePageNumberPagination

    @action(detail=False, url_path='my-profile')
    def profile(self, request):
        queryset = self.queryset.filter(id=self.request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])
