import random
r=random.randint(1,4)
s=int(input("Угадай, какой число от 1 до 4 я загадала? "))
if s==r:
    print("Победа!")
else:
    if s>r:
        print("Твое число больше, чем я загадала")
        print("Попробуй еще раз!")
    elif s<r:
        print("Твое число меньше, чем я загадала")
        print("Попробуй еще раз!")
      
