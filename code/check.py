pin = input('the pin you need check')
length = len(pin)
i = 0
if pin.isalpha():
    i += 1
if pin.isdigit():
    i += 1
if pin.isalnum() == 0:
    i += 1
if (i == 3) and (length >= 16) and (type(pin[0]) != int):
    print('高级密码')
if (i == 2 ) and (length >= 8):
    print('低级密码')
if (i == 1) and (length <= 8) and (pin.isalnum()):
    print('低级密码')
