import functools
@functools.lru_cache()
def fib(number):
     if number == 1 or number == 2:
         return 1
     else:
         return fib(number-1) + fib(number-2)

print(fib(50))

fibonacciCache = {}

def fibonacci(nthNumber):
    global fibonacciCache
    if nthNumber in fibonacciCache:
        return fibonacciCache[nthNumber]

    if nthNumber == 1 or nthNumber == 2:
        fibonacciCache[nthNumber] = 1
        return 1
    else:
        result = fibonacci(nthNumber-1)
        result = result + fibonacci(nthNumber- 2)
        fibonacciCache[nthNumber] = result
        return result

print(fibonacci(50))