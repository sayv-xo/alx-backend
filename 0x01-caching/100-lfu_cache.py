#!/usr/bin/env python3
"""LFU Caching Module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching
    Represents a LFU caching system where data are stored
    and can be retrieved from a dictionary
    """
    def __init__(self):
        """Instantiate a LFU caching system
        """
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """Adds item to the cache dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.count[key] += 1
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least = self.keys[0]
            for k in self.keys:
                if self.count[k] < self.count[least]:
                    least = k
            del self.cache_data[least]
            del self.count[least]
            self.keys.remove(least)
            print("DISCARD:", least)
        self.keys.append(key)
        self.cache_data[key] = item
        self.count[key] = 1

    def get(self, key):
        """Retrieves items from the cache dictionary"""
        if key in self.cache_data:
            self.count[key] += 1
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
