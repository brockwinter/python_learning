f1 = open('f:\\test.txt')
f2 = open('f:\\test1.txt', 'a+')
for each_line in f1:
    f2.write(each_line)

f1.close()
f2.close()

f2 = open('f:\\test1.txt')
print(f2.read())
