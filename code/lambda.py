def ds(x):
    return 2 * x + 1
print(ds(5))

lambda x: 2 * x + 1
g = lambda x: 2 * x + 1
print(g(5))

def add(x, y):
    return x+ y
print(add(3,4))

lambda x, y: x+y
g = lambda x, y: x+y
print(g(3, 4))

def fun(x, y=3):
    return x*y
print(fun(2))
print(fun(2, 5))

lambda x, y=3: x*y
g = lambda x, y=3: x*y
print(g(2))
print(g(2, 5))

lambda x: x if x%2 else None
g = lambda x: x if x%2 else None
print(g(10))

def odd(x):
    if x%2:
        return x
print(odd(10))

print(list(filter(lambda x: x % 3 == 0, range(0, 100))))

list(zip([1, 2, 3, 4, 5], [10, 11, 12, 13, 14]))

print(list(map((lambda x, y: [x, y]), [1, 2, 3, 4, 5], [10, 11, 12, 13, 14])))

