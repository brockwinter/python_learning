count = 5
def fun():
    count = 10
    print(count)
fun()
print(count)

count = 5
def fun():
    global count
    count = 10
    print(count)
fun()
print(count)