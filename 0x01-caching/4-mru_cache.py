#!/usr/bin/env python3
"""MRU Caching Module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching
    Represents a MRU caching system where data are stored
    and can be retrieved from a dictionary
    """
    def __init__(self):
        """Instantiate a MRU caching system
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds item to the cache dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop()
            del self.cache_data[last]
            print("DISCARD:", last)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the cache dictionary"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
