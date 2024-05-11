from collections import OrderedDict
from typing import Dict, Any


class Collection:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def update_capacity(self, new_capacity: int):
        self.capacity = new_capacity
        self._evict()

    def put(self, key: str, value: Any):
        if len(self.cache) >= self.capacity:
            self._evict()
        self.cache[key] = value
        # Move the recently accessed item to the end to mark it as the most recently used
        self.cache.move_to_end(key)

    def get(self, key: str) -> Any:
        if key in self.cache:
            # Move accessed item to end of OrderedDict (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def _evict(self):
        if len(self.cache) >= self.capacity:
            # Evict the least recently used item (the first item in the OrderedDict)
            self.cache.popitem(last=False)
