#!/usr/bin/env python3
"""Basic Cache Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching
    An object that represent a caching system where data are stored
    and can be retrieved from a dictionary
    """
    def put(self, key, item):
        """Adds item to the cache dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the cache dictionary"""
        return self.cache_data.get(key)
