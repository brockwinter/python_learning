def power(x,y):
    result = x ** y
    print(result)
    return
print(power(2,5))


def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t
        return x
    return
print(gcd(18,9))

def dtb(num):
    while num:
        str1 = '0'
        t = str(num % 2)
        num = num //2
        str1 += t
    return str1

print(dtb(10))
