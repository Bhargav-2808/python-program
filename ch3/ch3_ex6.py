import random

winn=random.randint(1,100)

enter=1

num=int(input("enter the number between 1 to 100 "))

game=False
while not game:
    if num==winn:
        print(F"you winn , guess it in {enter} times")
        game=True
    else:
        if num < winn :
            print("too low! ")
            enter +=1
            num=int(input("enter again : "))
        else :
            print("too high !")
            enter +=1
            num=int(input("enter again : "))
