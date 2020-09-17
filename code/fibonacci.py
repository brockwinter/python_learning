def fbnq(x):
    if x<0:
        print('error')
    elif x <= 2:
        return 1
    else:
        return fbnq(x-1)+fbnq(x-2)

print(fbnq(50))

x = 50
A = [1,1]
for i in range(3,x+1):
    A.append(A[i-2]+A[i-3])
print(A)
print(A[x-1])

