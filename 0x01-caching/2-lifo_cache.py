#!/usr/bin/env python3
"""LIFO Caching Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching
    Represents a LIFO caching system where data are stored
    and can be retrieved from a dictionary
    """
    def __init__(self):
        """Instantiate a LIFO caching system
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds item to the cache dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop()
            del self.cache_data[last]
            print("DISCARD:", last)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the cache dictionary"""
        return self.cache_data.get(key)
