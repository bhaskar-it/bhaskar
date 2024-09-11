import random
user=int(input("enter ur choice:'0' for paper,'1' for rock,'2' for seiocorres:"))
computer=random.randint(0,2)
print(f"user={user} and computer={computer}")
if computer == 0 and user ==2:
    print("you lose......")
elif computer == 2 and user == 0:
    print("you win !!!")
elif user == computer:
    print("its a draw......")
elif computer > user:
    print("you lose...")
elif computer < user:
    print("you win!!!")

    