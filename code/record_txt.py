def filewrite(file_name):
    print('请输入内容【单独输入‘:w’保存退出：')
    f = open(file_name,'w')
    while True:
        a = input()
        if a != ';w':
            f.write('%s\n' % a)
        else:
            break

    f.close()

file_name = input('请输入文件名：')
filewrite(file_name)