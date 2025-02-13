from cachetools import LRUCache
cache = LRUCache(maxsize=20)

def fibonacci_with_cache(num):
    if num in cache:
        return cache[num]

    if num < 2:
        return num
    else:
        cache[num] = fibonacci_with_cache(num-1) + fibonacci_with_cache(num -2)
        return cache[num]

print(fibonacci_with_cache(6))
print("Try Again!!")
print(fibonacci_with_cache(3))
print()
print(cache)