# n = eval(input())
# print ("{:->20,}".format(n))
# 第一题，格式化输出

#a = [3, 6, 9]
#b = eval(input())
#s = 0
#for i in range(3):
    #s += a[i] *b[i]
#print(s)

#import random
#random.seed(123)
#for i in range(10):
    #print(random.randint(1,999),end = ",")


#import turtle
#turtle.right(-30)
#turtle.fd(200)
#turtle.right(60)
#turtle.fd(200)
#turtle.right(120)
#turtle.fd(200)
#turtle.right(60)
#turtle.fd(200)

# data = input()
# info = {}
# i = 0
# man_num = 0
# age_total = 0
# while data:
#     info [i] = data.split(" ")
#     print(info)
#     i += 1
#     age_total += float(data.split(" ")[2])
#     if data.split(" ")[1] == '男':
#         man_num += 1
#     data = input()
# age_aver = age_total/i
# print("{:.2f}   {}".format(age_aver,man_num))

import os
fate = open('命运-网络版.txt', 'r', encoding= 'utf-8')
lines = fate.read()
fuhao = [' ', '\n', 'u3000']
#fuhao = [',', '.', '<', '>', '(', ')', '-', '《', '》', '\n' , ' ', '\u3000','，', '”', '“', '。', '：', '"']
d = {}
for word in lines:
    if word  not in fuhao:
        d[word] = d.get(word,0) + 1
    # else:
    #     d[word] = d.get(word,0) + 1
fate.close()
ls = list(d.items())
# print(type(ls))
# print(ls)
ls.sort(key= lambda x:x[1], reverse= True)
print ('{}:{}'.format(ls[0][0],ls[0][1]))
for i in range(10):
    print(ls[i][0], end='')
tongji = open('命运-频率统计.txt','w')
for a in ls:
    a_new = a[0] + ':' + str(a[1]) + ','
    tongji.write(a_new)
tongji.close()
f = open('命运-频率统计.txt','rb+')
f.seek(-1, os.SEEK_END)
f.truncate()
f.close()