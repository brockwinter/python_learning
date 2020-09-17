def dtb(num):
    str1 = ''
    while num:
        t = str(num % 2)
        num = num // 2
        str1 += t
    str1 = str1[::-1]
    return (str1)
print(dtb(10))

str1 =''
def dtb1(x):
    if x == 1:
        return '1'
    else:
        return str(x%2) + dtb1(x//2)

print(dtb1(10)[::-1])