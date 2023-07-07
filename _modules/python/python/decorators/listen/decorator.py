from functools import wraps
from typing import Callable, Iterable


def listen(parse_func: Callable):
    def decorate(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Iterable:
            while True:
                for event in func(*args, **kwargs):
                    yield parse_func(event)
        return wrapper
    return decorate
