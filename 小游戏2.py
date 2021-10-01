#小游戏2
import random
print("欢迎来到王文凯的游戏\n")
secert = random.randint(1,10)
guess = int(input("猜猜我想的是几："))  
count = 0
while guess != secert:
    count = count +1
    if count == 3:
         print("shit玩意又猜错了，拜拜了您嘞~~~")
         input()
         exit(0)
    if guess < secert:
         print("嘿，小了！小了！！")
    elif guess > secert:
         print("哥，大了大了~~")
    guess = int(input("诶呀，猜错了，请重新输入吧！："))
print("哇草，你是我心中的蛔虫吗？")
print("哼，猜中了也没有奖励")
print("游戏结束，不玩啦~~")
input()
