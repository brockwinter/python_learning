fi = open('sensor.txt', 'r+', encoding='UTF-8')
fo = open('earpa001.txt', 'w')
for line in fi:
    ls = line.strip("\n").split(',')
    if 'earpa001' in ls[1]:
        fo.write('{},{},{},{}\n'.format(ls[0], ls[1], ls[2], ls[3]))
fi.close()
fo.close()

fi = open('earpa001.txt', 'r', encoding='UTF-8')
fo = open('earpa001_count.txt', 'w')
d = {}
for line in fi:
    ls = line.strip('\n').split(',')
    temp = ls[2] + '-' + ls[3]
    d[temp] = d.get(temp, 0) + 1

ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in ls:
    temp = str(i[0]) + ',' + str(i[1]) + '\n'
    fo.write(temp)

fi.close()
fo.close()
