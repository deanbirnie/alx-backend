#!/use/bin/python3
"""
LIFO caching implementation
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initializes the LIFOCache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded = self.stack.pop()
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
