import random
import string
import time, secrets
from uuid import uuid4


def generate_uuid():
    return str(uuid4())


def generate_salt(nbytes: int = 40):
    return secrets.token_urlsafe(nbytes=nbytes)


def generate_password():
    return secrets.token_urlsafe(16)


def generate_session_key(nbytes=64):
    return generate_salt(nbytes=nbytes)


def generate_session_expiration(valid_window: int = 60 * 60 * 8):
    return int(time.time() + valid_window)


def current_int_timestamp():
    return int(time.time())


def generate_random_string(length: int = 10):
    return "".join(
        random.choice(string.digits + string.ascii_lowercase) for _ in range(length)
    )


def current_int_minute():
    return int(time.time() / 60)


def default_dict():
    return dict()
