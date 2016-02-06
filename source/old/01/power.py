def power_rec(a, n):
    if n < 0:
        return 1 / power(a, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        tmp = power(a, n // 2)
        return tmp ** 2
    else:
        return a * power(a, n-1)
        

def power_iter(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)

    return a * power(a, n-1)
    
power = power_rec
