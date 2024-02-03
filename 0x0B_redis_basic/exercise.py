#!/usr/bin/env python3
"""Redis basic"""
import redis
import uuid
from typing import Union


class Cache:
    """Function to write strings to Redis"""
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get_str(self, data):
        """Get the value from Redis using
        the get method with automatic conversion"""
        return data.decode("utf-8")

    def get_int(self, data):
        """Get the value from Redis and convert to int"""
        return int(data)
