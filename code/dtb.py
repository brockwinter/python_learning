def dtb(num):
    str1 = ''
    while num:
        t = str(num % 2)
        num = num // 2
        str1 += t
    str1 = str1[::-1]
    return (str1)
print(dtb(10))