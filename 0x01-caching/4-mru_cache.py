#!/usr/bin/python3
"""
MRU caching implementation
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initializes the MRUCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    del self.order[key]
                else:
                    discarded = next(reversed(self.order))
                    del self.cache_data[discarded]
                    del self.order[discarded]
                    print(f"DISCARD: {discarded}")

            self.cache_data[key] = item
            self.order[key] = True

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
