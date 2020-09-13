import random
# 随机数，有限次，猜数游戏
secret = random.randint(1 , 10)
print("--------------------")
guess = 0
i = 0
while (guess != secret) and (i < 3):
    temp = input("your answer")
    guess = int(temp)
    if guess == secret:
        print("right")
    else:
        if guess > secret:
            print("big")
        else:
            print('small')
    i = i + 1
print("game over")