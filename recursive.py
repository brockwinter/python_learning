def factorial(x):
    i = 1
    fa = 1
    while i<= x:
        fa *= i
        i += 1
    return fa
print(factorial(5))

def fac(x):
    if x == 1:
        return x
    else:
        return x * fac(x-1)
print(fac(5))

