import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class RegexValidator:
    def __init__(self, regex=None, min_length=6, max_length=20, message=""):
        if not regex:
            regex = "^[A-Za-z\d@$!#%*?&]{6,20}$"
            message = "Any alphanumeric and special character in @$!#%*?&"
        self.regex = regex
        self.message = message

    def validate(self, password, user=None):
        pattern = re.compile(self.regex)
        match = re.search(pattern, password)
        if not match:
            raise ValidationError(
                f"Password not valid : {self.message}",
                code='password_too_insecure',
                params={'message': self.message},
            )

    def get_help_text(self):
        return _(
            f"Format for password : '{self.message}'"
        )
