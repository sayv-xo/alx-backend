#!/usr/bin/env python3
"""LRU Caching Module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching
    Represents a LRU caching system where data are stored
    and can be retrieved from a dictionary
    """
    def __init__(self):
        """Instantiate a LRU caching system
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
            first = self.keys.pop(0)
            del self.cache_data[first]
            print("DISCARD:", first)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the cache dictionary"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
