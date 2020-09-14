i=1
while i <= 10000:
    if i % 7 == 0:
        if  i % 6 == 5:
            if i % 5 == 4:
                if i % 3 == 2:
                    if i % 2 ==1:
                        print(i)
                        i += 1
    i += 1
if i > 10000:
    print('find nothing')