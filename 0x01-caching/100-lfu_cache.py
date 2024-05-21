#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that uses LFU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.freq_map = {}
        self.min_freq = 0

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in
        self.cache_data is higher than BaseCaching.MAX_ITEMS:
        you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard,
        you must use the LRU algorithm to discard only the least recently used
        you must print DISCARD:\
                with the key discarded and following by a new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_map[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq_keys = [
                        key for key in self.cache_data
                        if self.freq_map[key] == self.min_freq]
                if len(min_freq_keys) > 1:
                    lru_key = min_freq_keys[0]
                    for k in min_freq_keys:
                        if self.freq_map[k] < self.freq_map[lru_key]:
                            lru_key = k
                    del self.cache_data[lru_key]
                    del self.freq_map[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    del self.cache_data[min_freq_keys[0]]
                    del self.freq_map[min_freq_keys[0]]
                    print(f"DISCARD: {min_freq_keys[0]}")

            self.cache_data[key] = item
            self.freq_map[key] = 1
            self.min_freq = 1

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t\
                exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_map[key] += 1
        self.min_freq = min(self.freq_map.values())
        return self.cache_data[key]


if __name__ == "__main__":
    LFUCache = __import__('100-lfu_cache').LFUCache

    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
