#!/usr/bin/env python3
""" FIFO Cache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching and implements
    FIFO caching
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
