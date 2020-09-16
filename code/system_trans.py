num = input('请输入你要转化的数')
num = num.upper()
while num != 'Q':
    if num.isdigit():
        num = int(num)
        print('十进制 ->十六进制：%d -> %#x' % (num, num))
        print('十进制 ->八进制：%d -> %#o' % (num, num))
        print('十进制 ->十六进制：{0} -> {1}', format(num, bin(num)))
        num = input('请输入你要转化的数')
    else:
        if num == 'Q':
            break
        else:
            print('输入不合法，请重输')

