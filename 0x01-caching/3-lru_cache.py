#!/usr/bin/python3
"""
LRU caching implementation
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initializes the LRUCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded = next(iter(self.order))
                    del self.cache_data[discarded]
                    del self.order[discarded]
                    print(f"DISCARD: {discarded}")
            elif key in self.cache_data:
                del self.order[key]

            self.cache_data[key] = item
            self.order[key] = True

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
