import string
import secrets


def keygen():
    alphabet = string.digits
    auth_code = ''.join(secrets.choice(alphabet) for _ in range(32))
    return auth_code


def slug_keygen():
    alphabet = string.ascii_letters + string.digits
    auth_code = ''.join(secrets.choice(alphabet) for _ in range(32))
    return auth_code
