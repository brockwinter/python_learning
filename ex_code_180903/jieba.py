import jieba
txt = input()
ls = jieba.lcut(txt)
print('{:.1f}'.format(len(txt)/len(ls)))