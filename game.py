import random


while True:
    try:
        level = int(input("Level:"))
        if level > 0:
            break
    except:
        pass

r = random.randint(1, level)
while True:
    try:
        g = int(input("Guess:"))
        if g < 1:
            continue
        if g > r:
            print("Too big :()")
        elif g < r:
            print("Too small :()")
        else:
            print("Just Right!")
            break
    except:
        pass