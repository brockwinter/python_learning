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
