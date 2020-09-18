f = open('f:\\testt.txt','rb')
# f.close() 关闭文件
# f.read(size = -1)
# 桌面
print(f)
# f.writelines('test')
# 获取当前光标位置
position_now = f.tell()
print("当前光标位置为：",position_now)
# 将光标移到开始位置
f.seek(0, 0)
text = f.read()
print(text)
f.close()
eight = 0o17
print(eight)
sixteen = 0X98
print(sixteen)
