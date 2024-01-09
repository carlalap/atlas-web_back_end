#!/usr/bin/python3
"""task4. MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class that inherits from BaseCaching"""

    def __init__(self):
        """Initializes the cache by calling
        the constructor of the base class
        & initializes instance variable self.__keys"""
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Method that add or update an item in the cache. Checks if the cache
        has reached its maximum capacity  """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Method get to retrieve an item
        from the cache based on the key."""
        if not key or key not in self.cache_data:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]
