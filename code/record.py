def file_new(boy, girl, count):
    file_name_boy = 'f:\\boy_' + str(count) + '.txt'
    file_name_girl = 'f:\\girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w', encoding='UTF-8')
    girl_file = open(file_name_girl, 'w', encoding='UTF-8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):

    f = open(file_name, encoding='UTF-8')
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            file_new(boy, girl, count)

            boy = []
            girl = []
            count += 1

split_file('f:\\test1.txt')


# 封装调用函数时，参数要明显准确，
#