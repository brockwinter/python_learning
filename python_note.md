# 小甲鱼学习笔记
## 一， 基础操作
### 一，print
1. print("")
2. print(5+3)，或直接输入5+3
3. print("river"+"well water")
4. print("river "*8)
5. print("river\n"*8)
   
### 二，
1. 缩进，tab,冒号后自动缩进
2. ==判断相等，=赋值
3. int()  可把字符串变成整形
4. input()输出一段字符串并把用户输入的赋值给左边
5. 流程图：圆框图输入输出，方框处理，菱形选择
6. BIF  built-in functions  
7. BIF查询  ：dir(__builtins__)   . 纯小写是bif
8. help (input)    中间是BIF名

```
print("--------------------")
temp = input("your answer")
guess = int(temp)
if guess == 8:
    print("right")
else:
    print("wrong")
print("game over")


name = input("plesae give me your name")
print("hello ,"+name+"!")


temp = input("give 0ne number from 1 to 100")
number = int(temp)
if number > 0 and number < 100:
    print("right")
else:
    print("wrong")

```
### 三，变量和字符串
变量，variable
字符串拼接
1. 变量使用前需要对其赋值
2. 变量名命名可以包括字母，数字，下划线，但不能以数字开头
3. 字母大小写不同
4. = 赋值，== 判断
5. 变量取名有意义

字符串，又叫文本，单双引号都好，但要配对
字符串中出现单双引号，可以用反斜杠转义\
\可对\转义

原始字符串;在字符串前边加上r,即可自动加\

长字符串，跨越多行的字符串，用三层引号字符串

注意用英文符号

```
first = 3
second = 8
third = first + second 
print(third)

mytea = "ll"
yourtea = "22"
ourtea = mytea +yourtea
print(ourtea)

print('c:\now')
print('c:\\now')
print(r'c:\now')

print('''a
b
c
d
''')
```

#### 四，条件分支,循环
1. 条件分支
比较操作符：!=, ==
输出是真假值，布尔值，0，1
用空格让程序美观易读
if 条件：
    条件为真(true)时执行的操作
else：
    条件为假(false)时执行的操作

```
print("--------------------")
temp = input("your answer")
guess = int(temp)
if guess == 8:
    print("right")
else:
    if guess >8:
        print("big")
    else:
        print('small')
print("game over")
```
2. while 循环
while 条件：
    条件为真(true)执行的操作


```
print("--------------------")
guess = 0
while guess != 8:
    temp = input("your answer")
    guess = int(temp)
    if guess == 8:
        print("right")
    else:
        if guess >8:
            print("big")
        else:
            print('small')
print("game over")
```

3. 逻辑操作符
and ,or .
？
比较操作符（大于小于）优先值高于逻辑操作符。
可以用括号标明优先操作顺序。

4. random模块
randint()

```
import random
secret = random.randint(1,10)
print("--------------------")
guess = 0
while guess != secret:
    temp = input("your answer")
    guess = int(temp)
    if guess == secret:
        print("right")
    else:
        if guess >secret:
            print("big")
        else:
            print('small')
print("game over")
```

习题部分

可用反斜杠或者括号把一行语句分解成多行
``` 
3 > 4 and \
1 < 2

(3 > 4 and 
1 < 2)
```

```
import random
secret = random.randint(1,10)
print("--------------------")
guess = 0
i = 0
while (guess != secret) and (i < 3):
    temp = input("your answer")
    guess = int(temp)
    if guess == secret:
        print("right")
    else:
        if guess >secret:
            print("big")
        else:
            print('small')
    i = i + 1
print("game over")
```
```
temp = input('请输入一个整数')
number = int(temp)
i = 0
while i < number:
    print(i+1)
    i = i + 1
```
```
temp = input('请输入一个整数')
number = int(temp)
while number >0:
    print(' '*(number-1)+'*'*number)
    number = number - 1
```

### 五，数据类型
#### 1，数值类型
1. 整形
2. 布尔类型，true,false
3. 浮点型
4. e记法，科学计数法，表示特别大或者特别小的数，产生浮点型
#### 2，类型转换
1. int()整数化，浮点变整数只保留整数
2. float() 浮点化
3. str()  字符串化

专用字尽量不要用作变量名
#### 3. 获得关于类型的信息
type(变量名)，可输出变量的数据类型
isinstance(变量名，数据类型)  判断该变量是不是这种数据类型


### 六，python常用操作符
#### 1，算术操作符
1. +
2. -
3. *
4. /  返回一个浮点型，精确的除数
5. %  取余
6. **  幂运算，优先级比左侧高，比右侧低
7. //   返回一个整数类型，地板除法
+= -= *= /=
8. 优先级问题，先加减，再乘除
   
#### 2.比较操作符
#### 3.逻辑操作符
and ,or , not
产生真假值，布尔值

#### 4.优先级问题
1. 幂运算 **
2. 正负号 + -
3. 算术操作符  * / //  +  -
4. 比较操作符
5. 逻辑操作符  not  > and  >or
   3 and 4 == 4 , 3 or 4 == 3

### 七，分支与循环
缩进
三元操作符
x if x < y else y
断言： assert  判断
如果判断为假，则自爆报错AssertionError
成员资格运算符，in

while 条件：
    循环体
    
 for循环
 for 目标 in  表达式：
    循环体
    
 range([start,] stop[, step=1])
 第三个参数默认值是1
 生成一个列表


中断，break，终止循环，跳出循环体
continue，终止本轮循环，开始下一轮循环

### 八，列表，一个打了激素的数组
#### 1.创建列表
1. 创建普通列表  member = ['A', 'B']
2. 创建混合列表  
3. 创建一个空列表  empty = []

#### 2. 向列表添加元素
1. append         member.append(一个元素)
2. extend         member.extend(待添加列表)
3. insert()       member.insert(位置，待添加元素)

#### 3.从列表中获取元素
1. 从列表中获取元素，member[索引值]
2. 从列表删除元素， remove()    member.remove(要删除的元素)
del     del member[待删除元素下标]
pop()    member.pop(下标)     弹出并返回一个值，若无下标默认最后一个
3. 列表分片(slice)
member[1:3：1]开始位置，结束位置，步长，包左不包右。
前后值都可以去。
member[:]拷贝一个列表

#### 4. 列表常见操作符
1. 比较操作符，比较第一个元素。字符串比较，比较ASC码
2. 连接操作符，左右类型一致，元组字符串可拼接。+
3. 重复操作符，*
4. 成员关系操作符  in , not in,返回布尔值
5. list.count(待寻找的元素)，数这个元素出现几次
6. list.index(待寻找元素，初始范围，结束范围)，找这个元素的下标
7. list.reverse()，列表元素翻转
8. list.sort() ，列表排序，从小到大排
sort(func, key)
sort(reverse=true) ,列表排序，从大到小排

### 九，元组，戴上了枷锁的列表
列表可任意插入，删除元素，但列表不可
1. 创建，列表用[].元组用()
2. 通过下标访问元素，切片

列表的逗号是关键temp = (1, )
temp = 1, 2, 3
temp = ()
temp = 1,

更新和删除一个元组
用切片和拼接 

### 十，字符串的内置方法
字符串定下了就不能改，和元组一样，需要修改的话可以切片重建
1. capitalize()      str.capitalize()       首字母大写
2. str.casefold()     所有字符变小写
3. str.center(width)   将字符串居中，使用空格填充至长度为width的新字符串
4. str.count(sub[,start[,end]])   返回sub在字符串里边出现的次数，start和end参数表示范围，可选。
5. str.endswith(sub[,start[,end]])  检查是否是以sub结尾
6. str.expandtabs([tabssize=8])     把字符串里的tab(\t)符号转化为空格，如不指定参数，默认空格数是tabsize = 8
7. str.find(sub[,start[,end]])    检测sub是否在字符串中，是则返回索引值，否则返回-1
8. str.index(sbu[,start[,end]])   同find，若未找到返回一个异常
9. str.isalnum()      如果字符串至少有一个字符，并且所有字符都是数字或字母，则返回true，否则返回false
10. str.isalpha()     如果字符串至少有一个字符，并且所有字符都是字母，则返回true,否则false
11. str.isdecimal()    如果字符串只包含十进制数字则返回true，否则返回false
12. str.isdigit()      如果字符串只包含数字则返回true， 否则返回false
13. str.islower()       如果字符串至少包含一个区分大小写的字符，并且这些字符都是小写，则返回true,否则返回false
14. str.isnumeric()      如果字符串只包含数字字符，则返回true,否则返回false
15. str.isspace()        如果字符串只包含空格，则返回true,否则返回false
16. str.istitle()       如果字符串都是标题化，（所有的单词都是以大写开始，其余字母均小写），则返回true,否则返回false
17. str.isupper()      如果字符串至少包含一个区分大小写的字符，并且这些字符都是大写，则返回true,否则返回false
18. str.join(sub)      以字符串作为分隔符，插入到sub所有的字符中
19. str.ljust(width)    返回一个左对齐的字符串，并使用空格填充长度为width的新字符串
18. str.lower()          所有大写字母变小写
19. str.lstrip()        去掉字符串左边的所有空格
20. str.rstrip()        去掉字符串右边的所有空格
21. str.partition(sub)   找到字符串sub，把字符串分成一个3元组(pre_sub, sub, fol_sub)
22. str.replace(old,new,[,count])     把字符串中的old字符串替换成new字符串，如果count指定，则替换不超过count次
23. rfind(sub[,start[,end]])     类似find，但是从右开始找
24. rindex(sub[,start[,end]])    类似index，但是从右开始找
25. rpartition(sub)           类似partition，但是从右开始找
26. split(sep=None,maxsp=-1)   不带参数默认是以空格为分隔符切片字符串，如果maxsplit参数指定，则仅分割maxsplit个子字符串，返回切片后的子字符串拼接的列表
27. splitlines(([keepends]))    按照\n分割，返回一个包含各行作为元素的列表，如果keepends参数指定，则返回前keepends行
28. startwith(prefix[,start[,end]])   检查是否以prefix开头
29. strip([chars])      删除字符串前边后边所有空格，chars参数可以定制删除的字符
30. swapcase()          反转字符中的大小写
31. title()             返回标题化的字符串
32. upper()             所有字母大写
33. zfill(wideth)         返回长度为width的字符串，原字符串右对齐，前边用0填充

### 十一，字符串的格式化
按照统一的规格输出字符串

"{0} love {1}.{2}".format("I", "FISHC", "COM")
1. %c   格式化字符及其ASCII码
2. %s   格式化字符串
3. %d   格式化整数
4. %o   格式化无符号八进制数
5. %x   格式化无符号十六进制数
6. %f   格式化定点数，可指定小数点后精度
7. %e   格式化科学计数法,格式化浮点数
8. %g   根据值的大小用%f 或%e

1.m.n     m是显示的最小总宽度， n是小数点后的位数
2. - 用于左对齐
3. + 在正数前面显示正号
4. # 在八进制前显示0o，十六进制前显示0x
5. 0 显示的数字前面填充0，取代空格
print('%#o' % 15)
print('%#x' % 15)

1. \'
2. \"
3. \a  发出系统响铃
4. \n  换行符
5. \t  横向制表符（TAB）
6. \v  纵向制表符
7. \r  回车符
8. \f  换页符
9.  \o 八进制数代表的字符
10. \x 十六进制数代表的字符
11. \0 表示一个空字符
12. \\ 反斜杠

### 十二，序列
列表，元组和字符串的共同点：
1. 通过索引得到元素
2. 索引值从0开始
3.分片
4.共同操作符：重复，拼接，成员关系

list()   列表化
tuple()  元组化
str()    字符串化
len()    返回参数中元素个数
max()    返回序列中的最大值，字母返回ASCII码值
min()     返回序列中的最小值，字母返回ASCII码值，要保证数据类型一致
sum(interable[,start=0])     返回序列的总和,再加上start
sorted()     排序，默认从小到大
reversed()   返回一个迭代器
      d = list(reversed(c))
enumerate()   返回索引值和本值
        e = list(enumerate(c))
zip() f = list(zip(b, c))

###十三，函数
1. 定义函数：
def MyFirstFunction():
    print('I Love It')
调用函数

2.函数参数
def MySecondFunction(name):# 这里的name是形参
    print(name + 'love')
MySecondFunction('s ')#这里的's'是实参

3,函数的返回值
def add(a,b):
    return (a + b)
print(add(10,15))

4. 函数文档
def add(a,b):
    '这里是函数文档'
    return (a + b)
print(add.__doc__)

5. 关键字参数
def add(a,b):
    return (a + b)
print(add(a=10,b=15))#这里的a,b都是关键字参数

6，默认参数
def add(a=10,b=15):#这里的10，15是默认参数
    return (a + b)
print(add())#这里没参数就输出默认参数，有参数就用这个参数

7. 收集参数
def test(*params):
    print('c参数的长度是：',len(params))
    print('第二个参数是',params[1])
print(test(1,2,5,8,9,3.2,25,10))

return,函数结束行

8,python 只有函数没有过程

9. 变量的作用域
定义函数里的变量作用范围只在定义函数里生效。局部变量
全局变量，可以作用在定义函数内
如果在定义函数里试图修改全局变量，python会自动生成一个局部变量代替

真的要在定义函数里改变全局变量的话，用global声明一下就好

count = 5
def fun():
    global count
    count = 10
    print(count)
fun()
print(count)

10.内嵌函数
定义函数内部再定义函数
内定义函数只能在本定义函数里调用，在外部不能被调用

11. 闭包closure
不能在内置函数里调用外部变量
nonlocal,声明一下不是局部变量就可以在内部函数调用全局变量

12. 匿名函数lambda
lambda x, y: x+y
g = lambda x, y: x+y
print(g(3, 4))
省下定义函数的时间

13. 两个厉害的bif
filter()
# print(help(filter))
filter(None, [1, 0, False, True])
print(list(filter(None, [1, 0, False, True])))
filter 两个参数，第一个参数为none时，可过滤掉第二个参数里为假的东西
filter第一个参数可以定制

print(list(filter(lambda x: x % 2, range(10))))

14.map()
print(list(map(lambda x: x % 2, range(10))))