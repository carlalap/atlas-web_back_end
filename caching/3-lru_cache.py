#!/usr/bin/python3
"""task3. LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initializes the cache by calling the constructor
        of the base class (super().__init__()
        & Initializes instance variables"""
        super().__init__()
        self.head, self.tail = "-", "="
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """Method that set up the initial linked list structure
        with the provided head and tail nodes."""
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """Removes a key from the cache, updating
        the linked list accordingly."""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """ Adds a new key and item to the cache.
        Inserts the new key between the tail
        and the previous node of the tail."""
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def put(self, key, item):
        """Add or update an item in the cache."""
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """Retrieve an item from the cache based on the key."""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
