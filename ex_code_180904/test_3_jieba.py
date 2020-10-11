import jieba
txt = input()
ls = jieba.lcut()
for i in ls[::-1]:
    print(i, end='')