import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8 or \
           not re.search(r'[A-Z]', password) or \
           not re.search(r'[a-z]', password) or \
           not re.search(r'[0-9]', password) or \
           not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                _("Password must contain at least 8 characters, one uppercase, one lowercase, one digit, and one special character."),
                code='password_invalid'
            )

    def get_help_text(self):
        return _(
            "Must contain at least 8 characters, one uppercase, one lowercase, one digit, and one special character."
        )
