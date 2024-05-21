#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that uses LRU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]


if __name__ == "__main__":
    LRUCache = __import__('3-lru_cache').LRUCache

    my_cache = LRUCache()
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
