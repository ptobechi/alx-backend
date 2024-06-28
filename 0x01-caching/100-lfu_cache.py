#!/usr/bin/env python3
""" LFU Cache module """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and
    implements LFU caching
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, freq in self.frequency.items() if freq == min_freq]

                # If there are multiple LFU items, use LRU among them
                if len(lfu_keys) > 1:
                    lfu_lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    lfu_lru_key = lfu_keys[0]

                del self.cache_data[lfu_lru_key]
                del self.frequency[lfu_lru_key]
                del self.usage_order[lfu_lru_key]
                print(f"DISCARD: {lfu_lru_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.usage_order[key] = len(self.usage_order) + 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order[key] = len(self.usage_order) + 1
        return self.cache_data[key]
