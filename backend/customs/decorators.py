import time
from django.core.cache import caches
from functools import wraps
from backend.customs.exceptions import CustomException
from backend.services.routine_timing import set_routine_time
from backend.services.telegram_messages import simple_log

cache = caches["cache_lock"]


class LockedKeyException(CustomException):
    pass


def generate_key(function_name, **kwargs):
    keywords = "".join(f"{key}_{kwargs[key]}" for key in kwargs)
    return f"{function_name}_{keywords}"


def accuire_lock(key, expire: float = None):
    return cache.add(key, True, expire)


def release_lock(key):
    return cache.delete(key)


def locked_process(expire_time: float = None, identifier: str = None):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = generate_key(function_name=func.__name__, **kwargs)
            if identifier:
                key += f"_{identifier}"
            if not accuire_lock(key=key, expire=expire_time):
                simple_log(message=f"processs is locked! name: {key}", level="log")
                return
            try:
                result = func(*args, **kwargs)
                release_lock(key=key)
                return result
            except:
                release_lock(key=key)
                raise

        return wrapper

    return decorate


def timed_routine():
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            set_routine_time(
                routine_name=func.__name__, elapsed_time=end_time - start_time
            )
            return result

        return wrapper

    return decorate
