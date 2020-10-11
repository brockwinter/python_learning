fi = open('PY301-SunSign.csv', 'r')
st = fi.read()
ls = st.split('\n')
ls1 = []
del ls[0]
for i in range(len(ls)):
    ls1.append(ls[i].split(','))
name = input("请输入星座中文名称")
for i in range(len(ls1)):
    if name in ls1[i]:
        temp = i
print(name + '的生日位于' + ls1[temp][2] + '-' + ls1[temp][3] + '之间')