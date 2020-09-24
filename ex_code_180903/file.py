fi = open('论语.txt', 'r')
fo = open('论语-原文.txt' ,'w')
wflag = False
for line in fi:
    print(type(line))
    if '【' in line:
        wflag = False###用wflag将此循环的判断延续到下一回合
    if '【原文】' in line:
        wflag = True
        continue
    if wflag == True:
        line = line.strip('')
        if line.count('\n') != len(line):##不是空行才写入
            print(len(line))
            fo.write(line)
fi.close()
fo.close() 

fi = open('论语-原文.txt', 'r')
fo = open('论语-提纯原文.txt', 'w')
ls = []
for line in fi:
    ls = list(line)
    ls1 = ''
    for word in ls:
        if word == '(' or word == ')' or word.isdigit():
            continue
        else:
            ls1 = ls1 +str(word)
    fo.write(ls1)
fi.close()
fo.close()