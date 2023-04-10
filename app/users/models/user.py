from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..manager import UserManager
from ...commons.models import BaseModel

unicode_validator = UnicodeUsernameValidator()


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_('email address'), unique=True, blank=False)
    phone = models.CharField(_('phone'), max_length=20, null=True, blank=True)
    first_name = models.CharField(_('first_name'), max_length=90, blank=False, null=False)
    middle_name = models.CharField(_('middle_name'), max_length=80, blank=True, null=True)
    last_name = models.CharField(_('last_name'), max_length=70, blank=False, null=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether users can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this users should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('users')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.first_name} {self.middle_name if self.middle_name else ""} {self.last_name}'
