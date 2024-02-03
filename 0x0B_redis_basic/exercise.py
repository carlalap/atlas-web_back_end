#!/usr/bin/env python3
"""Redis basic"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Method takes a single method Callable
    argument and returns a Callable."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """increments the count for that key every time
        the method is called and returns the value
        returned by the original method."""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Method that store the history of inputs
    and outputs for a particular function."""
    key = method.__qualname__
    input_key = key + ":inputs"
    output_key = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapped function to retrieve the output"""
        self._redis.rpush(input_key, str(args))
        # return output
        routput = str(method(self, *args, **kwds))
        self._redis.rpush(output_key, routput)

        return routput
    return wrapper


def replay(method: Callable):
    """display the history of calls
    of a particular function"""
    key = method.__qualname__
    input_key = key + ":inputs"
    output_key = key + ":outputs"
    redis = method.__self__.redis
    counts = redis.get(key).decode("utf-8")
    print(f"{key} was called {counts} times:")
    list_in = redis.lrange(input_key, 0, -1)
    list_out = redis.lrange(input_key, 0, -1)
    zip_list = list(zip(list_in, list_out))
    for a, b in zip_list:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """Function to write strings to Redis"""
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key using uuid"""
        key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """Take a key string argument to convert later
        the data back to the desired format."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """Get the value from Redis using
        the get method with conversion a UTF-8"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Get the value from Redis and convert to int"""
        data = self._redis.get(key)
        try:
            return int(data) if data is not None else None
        except (ValueError, TypeError):
            return None
