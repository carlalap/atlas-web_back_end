#!/usr/bin/python3
"""task2. LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFO caching system with methods to add, update,
    and retrieve items from the cache."""
    def __init__(self):
        """Initializes the cache by calling the constructor
        of the base class"""
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """The method Put add or update an item in the cache."""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """Get method that retrieve an item from the
        cache based on the key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
