from django.core.exceptions import ValidationError


def me_validator(value):
    if value == 'me':
        raise ValidationError(
            '%(value)s недопустимое имя',
            params={'value': value},
        )
