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



