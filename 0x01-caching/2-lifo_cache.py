#!/usr/bin/env python3
""" LIFO Cache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    and implements LIFO caching
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
