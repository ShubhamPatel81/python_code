import random

# 0 for snake , 1 for water , 2 for gun


def check(computer, user):
    if (computer == user):
        return 0
    elif (computer == 0 and user == 1):
        return -1
    elif (computer == 1 and user == 2):
        return -1
    elif (computer == 2 and user == 0):
        return -1
    return 1


computer = random.randint(0, 2)
user = int(input("Enter : 0 - for snake \n 1- for water \n 2- for Gun \n"))
score = check(computer, user)
print('Your choice : ', user)
print('Computer  choice : ', computer)
if (score == 0):
    print("Draw ")
elif (score == -1):
    print("you loose")
else:
    print("you won ")
