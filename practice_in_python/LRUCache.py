from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):

        self.size = capacity

        self.lru_cache = OrderedDict()

    def get(self, key: int) -> int:

        if key not in self.lru_cache:
            return -1

        else:
            # refresh the entry with given key
            self.lru_cache.move_to_end(key)

            return self.lru_cache[key]

    def put(self, key: int, value: int) -> None:

        if key not in self.lru_cache:

            if len(self.lru_cache) >= self.size:
                # pop the least used entry
                self.lru_cache.popitem(last=False)

        else:
            # refresh the entry with given key
            self.lru_cache.move_to_end(key)

        self.lru_cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
