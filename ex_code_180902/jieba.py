import jieba
s = input()
n = len(s)
m = len(jieba.lcut(s))
print("{} {}".format(n, m))