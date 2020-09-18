num2 = {1, 2, 3, 4}
print(type(num2))

num1 = {1, 2, 2, 3, 3, 4}
print(num1)

# 不支持索引

set1 = set([1, 2, 3, 5, 1])
print(set1)

# 去除重复元素
num2 = [1,2,3,4,5]
temp = []
for each in num2:
    if each not in temp:
        temp.append(each)
print(temp)

num2 = list(set(num2))
print(num2)
num3 = set(num2)
num3.add(6)
print(num3)

num4 = frozenset([1, 2, 3, 4])#不能添加