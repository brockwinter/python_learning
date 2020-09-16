def findstr():
    temp = input("请输入总字符串")
    str1 = input("请输入待寻找字符串")
    n = 0
    for i in range(len(temp)-1):
        if temp[i] ==str1[0] and temp[i+1] == str1[1]:
            n += 1
    print(n)
    return
print(findstr())