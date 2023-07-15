import random

response = "y"

while response == "y":
   
    dice_number = random.randint(1, 6)
    
 
    if dice_number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    elif dice_number == 2:
        print("---------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("---------")
    elif dice_number == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")
    elif dice_number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    elif dice_number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    elif dice_number == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")

    response = input("Do you want to roll the dice again? (y/n): ")

print("Thank you for playing!")