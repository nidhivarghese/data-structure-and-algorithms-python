def addto80(n):
    return 80 + n

# Using Cache Dictionary
cache = dict()
def memoizedAddto80(n):
    if n in cache:
        return cache[n]
    else:
        print("Long Time!")
        cache[n] = 80 + n
        return cache[n]

print(memoizedAddto80(5))
print(memoizedAddto80(5))

# Using LRU Cache
from functools import lru_cache
@lru_cache(maxsize=5)
def squaring_with_cache(n):
    print("Long Time!!")
    return n*n

print(squaring_with_cache(5))
print(squaring_with_cache(5))
print(squaring_with_cache.cache_info())