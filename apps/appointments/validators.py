import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError('Введите правильный номер телефона.')