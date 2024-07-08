from django.core.exceptions import ValidationError
import re

def validate_name(value):
    if not re.match(r'^[a-zA-Zа-яА-ЯёЁ]+$', value):
        raise ValidationError(
            '%(value)s содержит недопустимые символы. Разрешены только буквы.',
            params={'value': value},
        )

def validate_passport_number(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError(
            '%(value)s содержит недопустимые символы. Разрешены только цифры.',
            params={'value': value},
        )