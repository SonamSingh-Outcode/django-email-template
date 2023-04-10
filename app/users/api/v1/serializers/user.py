from django.contrib.auth.models import Permission
from rest_framework import exceptions
from rest_framework import serializers

from app.commons.dynamic_serializer import DynamicFieldsModelSerializer
from ....constants import ADMIN, USER
from ....models import User


class UserCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_superuser')
        read_only_fields = ('id',)


class UserSerializer(DynamicFieldsModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'email',
                  'phone', 'permissions', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('id',)

    def get_permissions(self, instance):
        permission = Permission.objects.filter(user=instance.id).values_list('codename', flat=True)
        if permission:
            return permission
