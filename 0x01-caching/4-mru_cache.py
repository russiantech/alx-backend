#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that uses MRU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS:
        you must discard the most recently used item (MRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]


if __name__ == "__main__":
    MRUCache = __import__('4-mru_cache').MRUCache

    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
