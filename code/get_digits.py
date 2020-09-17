def my_get_digits(n):
    stra = str(n)
    A =[]
    for i in range(0,len(stra)):
        A.append(int(stra[i]))
    return A
print(my_get_digits(12345))

A = []
def fish_get_digits(n):
    if n > 0:
        A.insert(0,n%10)
        return fish_get_digits(n // 10)
fish_get_digits(12345)
print(A)