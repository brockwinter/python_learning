def dn():
    print('三位数的水仙花为：')
    temp = 100
    while temp < 1000:
        sub = (temp // 100 )**3 +((temp %100)//10)**3+(temp%10)**3
        if sub == temp:
            print(temp)
        temp += 1
    return
dn()
