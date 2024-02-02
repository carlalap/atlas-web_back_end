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
