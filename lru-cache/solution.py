from time import time

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.feq_cache = dict()
    
    def is_full(self):
        return len(self.cache) == self.size

    def get(self, key: int) -> int:
        if key in self.feq_cache:
            self.feq_cache[key] = time()
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.is_full() and key not in self.cache:
            _key = min(self.feq_cache, key=self.feq_cache.get)
            del self.cache[_key]
            del self.feq_cache[_key]
        self.cache[key] = value
        self.feq_cache[key] = time()