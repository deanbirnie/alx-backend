#!/usr/bin/python3
"""
LFU caching implementation
"""
from collections import defaultdict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initializes the LFUCache
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.frequency_count = defaultdict(int)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    least_freq = min(self.frequency.values())
                    items_to_discard = [k for k, v in self.frequency.items()
                                        if v == least_freq]
                    if len(items_to_discard) > 1:
                        least_recently_used = min(self.frequency_count.get(k,
                                                                           0)
                                                  for k in items_to_discard)
                        items_to_discard = [k for k in items_to_discard if
                                            self.frequency_count.get(k, 0)
                                            == least_recently_used]
                    discard_key = items_to_discard[0]
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    del self.frequency_count[discard_key]
                    print(f"DISCARD: {discard_key}")

                self.cache_data[key] = item
                self.frequency[key] = 1

            self.frequency_count[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
