#!/usr/bin/python3
"""Task0. Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class that inherits from BaseCaching and is a
    caching system, it uses put & get methods """
    def put(self, key, item):
        """ Assign to the dictionary self.cache_data.."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
