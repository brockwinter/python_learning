def funx(x):
    def funy(y):
        return x*y
    return  funy
i = funx(8)
print(i)
print(type(i))
print(i(5))
print(funx(8)(5))

def funx():
    x = [5]
    def funy():
        x[0] *= x[0]
        return x
    return funy()
print(funx())

def funx():
    x = 5
    def funy():
        nonlocal x
        x *= x
        return x
    return funy()
print(funx())