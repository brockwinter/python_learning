print("--------------------")
\
temp = input("your answer")
guess = int(temp)
if guess == 8:
    print("right")
else:
    print("wrong")
print("game over")


name = input("plesae give me your name")
print("hello ,"+name+"!")

temp = input("give 0ne number from 1 to 100")
number = int(temp)
if number > 0 and number < 100:
    print("right")
else:
    print("wrong")