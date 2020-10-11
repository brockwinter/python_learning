fi = open('PY301-SunSign.csv', 'r')
st = fi.read()
ls = st.split('\n')
ls1 = []
del ls[0]
for i in range(len(ls)):
    ls1.append(ls[i].split(','))
while True:
    number = input("请输入星座编号")
    ls = number.split(' ')
    for k in ls:
        k = int(k) - 1
        print(ls1[k][1], end='')
        print('(',end='')
        print()
        # st = ls1[k][1] + ls1[k][4] +'的生日是{}月{}日至{}月{}日之间'.format(, ls[k][4], ls[k][2][:-2]), ls[k][2][-2:], ls[k][3][:-2]), ls[k][3][-2:])
        # print(st)