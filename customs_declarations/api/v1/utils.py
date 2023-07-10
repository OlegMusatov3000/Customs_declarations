import string
import secrets
from django.core.mail import send_mail

from customs_declarations.settings import EMAIL_API


def send_confirmation_code(email, confirmation_code):
    """Oтправляет на почту пользователя код подтверждения."""
    send_mail(
        subject='Код подтверждения',
        message=f'ваш "confirmation_code": {confirmation_code}',
        from_email=EMAIL_API,
        recipient_list=(email,),
        fail_silently=False,
    )


def keygen():
    """Генерирует числовое значение."""
    alphabet = string.digits
    auth_code = ''.join(secrets.choice(alphabet) for _ in range(32))
    return auth_code


def slug_keygen():
    """Генерирует буквенно-числовое значение."""
    alphabet = string.ascii_letters + string.digits
    auth_code = ''.join(secrets.choice(alphabet) for _ in range(32))
    return auth_code
