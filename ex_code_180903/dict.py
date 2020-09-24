txt = input()
ls = txt.split(' ')
d = {}
for i in ls:
    d[i] = d.get(i, 0) + 1
ls = list(d.items())
ls.sort(key= lambda x:x[1], reverse = True)
for k in ls:
    print('{}:{}'.format(k[0],k[1]))