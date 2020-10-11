txt = input('请输入科目成绩')
d = {}
r = 0
while txt:
    ls = txt.split(' ')
    d[ls[0]] = ls[1]
    txt = input("请输入下一项")
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
print('最高课程是'+ls[0][0] + ls[0][1], end=',')
print('最低成绩是'+ls[(len(ls)-1)][0]+ ls[(len(ls)-1)][1], end=',')
for i in range(len(ls)):
    r += int(ls[i][1])
print(('平均成绩是{:.2f}'.format(r/(len(ls)))), end='.')
# txt = 'shuxue 90'
# ls = txt.split(" ")
# print(ls)