#!/usr/bin/python3
"""task1. FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def _popMethod(self):
        """Remove of the oldest item in the cache
        based on the FIFO algorithm."""
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _pushMethod(self, key, item):
        """Add a new item to the cache based on the FIFO algorithm"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._popMethod()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """ add or update an item in the cache."""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._pushMethod(key, item)

    def get(self, key):
        """Retrieve an item from the cache based on the key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
