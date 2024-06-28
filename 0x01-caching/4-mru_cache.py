#!/usr/bin/env python3
""" MRU Cache module """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    and implements MRU caching
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
            # Remove the existing key to update its order
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            discarded_key = self.order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end of the order list
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
