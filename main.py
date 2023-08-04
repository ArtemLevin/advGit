import functools
@functools.lru_cache()
def fib(number):
    if number == 1 or number == 0:
        return 1
    else:
        return fib(number-1) + fib(number-2)

print(fib(15))
