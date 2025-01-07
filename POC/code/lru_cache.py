from functools import lru_cache

class HeavyComputation:
    def __init__(self, x):
        self._x = x

    @lru_cache(maxsize=None)
    def result(self):
        print("Performing expensive computation...")
        return self._x ** 2  # Expensive operation

    def update_x(self, new_x):
        self._x = new_x
        self.result.cache_clear()  # Clear the cache when _x changes

# Usage
obj = HeavyComputation(5)
print(obj.result())  # Output: Performing expensive computation... 25
print(obj.result())  # Output: 25 (cached)
obj.update_x(10)
print(obj.result())  # Output: Performing expensive computation... 100
