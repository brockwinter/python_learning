n = eval(input())
if n == 1:
    cost = 160*n
elif (1<n) and (n<5):
    cost = 160*n*0.9
elif (4<n) and (n<10):
    cost = 160*0.8*n
elif n>9:
    cost = 160*0.7*n
cost = int(cost)
print(cost)