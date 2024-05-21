#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that doesn't have limit
    """

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    BasicCache = __import__('0-basic_cache').BasicCache

    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
