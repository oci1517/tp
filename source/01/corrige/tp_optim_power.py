from __future__ import print_function
from time import time

def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)

    return a * power(a, n-1)

def power_iter(a, n):
    result = 1

    if n < 0:
        return 1 / power_iter(a, -n)
        
    for i in range(n):
        result = result * a

    return result

def fast_power(a, n):
    if n < 0:
        return 1 / fast_power(a, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        tmp = fast_power(a, n // 2)
        return tmp ** 2
    else:
        return a * fast_power(a, n-1)
    
def chrono_power():
    power(1.5123, 512)
    
def timeit(function, n=10):
    times = [0] * n
    for i in range(n):
        t0 = time()
        function()
        t1 = time()
        times[i] = t1 - t0
        
    return sum(times) / len(times)
    
print(timeit(lambda : power(1.5, 512), n=10))

print(80*"*")
print("Comparison")

print(timeit(lambda: power(1.5, 600), n=1000))
print(timeit(lambda: fast_power(1.5, 511), n=1000))
print(timeit(lambda: fast_power(1.5, 512), n=1000))

print(timeit(lambda : power(2, 500)))
print(timeit(lambda : power_iter(2, 500)))