def MyFirstFunction():
    print('I Love it')
MyFirstFunction()


def MySecondFunction(name):
    print(name + 'love')
MySecondFunction('s ')

def add(a,b):
    result = a + b
    print(result)
add(10,15)

def add(a,b):
    return (a + b)
print(add(10,15))


def add(a,b):
    '这里是函数文档'
    return (a + b)
print(add.__doc__)

def test(*params):
    print('c参数的长度是：',len(params))
    print('第二个参数是',params[1])
print(test(1,2,5,8,9,3.2,25,10))

def test(*params,exp):
    print('c参数的长度是：',len(params))
    print('第二个参数是',params[1])

print(test(1,2,5,8,9,3.2,25,exp=10))