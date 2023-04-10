import uuid

from cuser.fields import CurrentUserField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

unicode_validator = UnicodeUsernameValidator()


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(_('is_deleted'), default=False, )

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True


class CuserModel(models.Model):
    created_by = CurrentUserField(
        add_only=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
        null=True
    )

    updated_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        abstract = True


class CustomPrimaryKey(models.Model):
    id = models.UUIDField(max_length=150, primary_key=True, validators=[unicode_validator], default=uuid.uuid4,
                          editable=False)

    class Meta:
        abstract = True


class BaseModel(CuserModel, TimeStampModel, SoftDeleteModel, CustomPrimaryKey):
    class Meta:
        ordering = '-updated_at',
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)
