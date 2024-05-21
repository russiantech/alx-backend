#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that uses LIFO algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data\
            is higher than BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD:\
            with the key discarded and following by a new line
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and
        len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t\
            exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    LIFOCache = __import__('2-lifo_cache').LIFOCache

    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
