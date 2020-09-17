# print(help(filter))
filter(None, [1, 0, False, True])
print(list(filter(None, [1, 0, False, True])))

def odd(x):
    return x % 2
temp = range(10)
print(type(temp))
show = filter(odd, temp)
print(type(show))
print(list(show))

print(list(filter(odd, temp)))
print(list(filter(lambda x: x % 2, range(10))))

print(list(map(lambda x: x % 2, range(10))))