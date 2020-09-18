dirt1 = {'a': 'fast', 'b': 'low'}
print('a')
print(dirt1['a'])
dirt2 = {('a', 'fast'), ('b', 'low')}
dirt3 = dict(a= 'fast', b ='low')

dirt3['a'] = '1245'
print(dirt3)

dict1 = {}
dict1 = dict1.fromkeys((1, 2, 3))

dict2 = {}
dict2 = dict2.fromkeys((1, 2, 3), 'numbers')


dict3 = {}
dict3 = dict3.fromkeys((1, 2, 3), ('one', 'two', 'three'))

print(dict1)
print(dict2)
print(dict3)

dict1.fromkeys((1, 3), '数字')
print(dict1.fromkeys((1, 3), '数字'))
# 创造一个新的字典

dict1 = dict1.fromkeys(range(32), '赞')
print(dict1)
for eachkey in dict1.keys():
    print(eachkey)

for eachvalue in dict1.values():
    print(eachvalue)

for eachItem in dict1.items():
    print(eachItem)

print(dict1[0])

print(dict1.get(32))
print(dict1.get(32, '没有'))
print(31 in dict1)
print(32 in dict1)

dict1.clear()
print(dict1)
# 清空字典可以用clean

a = {1: 'one', 2: 'two', 3: 'three'}
b = a.copy()   #这是浅拷贝
c = a  #这是赋值

print(id(a), id(b), id(c))
c[4] = 'four'
print(a, b, c)#  b没有改变，ac改变了

a.pop(2)
print(a)#  2对应的项就没有了

a.popitem()
print(a)  # 随机弹出来一项

a.setdefault('小白')
print(a) # 添加一项key为小白的

a.setdefault(5, 'five')
print(a)# 添加一项5five

b = {'小白': '狗'}
a.update(b)   # 用小字典更新大字典
print(a)


