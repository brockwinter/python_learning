def fun1():
    print("fun1 is being called")
    def fun2():
        print('fun2 is being called')
    fun2()
fun1()
