import random

choices = ['stone','paper','scissors']

while True:
    num = random.randrange(0,3)
    
    print("Enter 1 for stone \nEnter 2 for paper \nEnter 3 for scissors \nEnter 0 to exit")
    
    inp = int(input())
    
    if inp == 0:
        print("Thanks for playing")
        break
    
    if 1 <= inp <= 3:
        
        user_choice = inp - 1
        
        if user_choice == num:
            print(f"You tied: {choices[user_choice]} vs {choices[num]}")
        elif (user_choice == 0 and num == 2) or (user_choice == 1 and num == 0) or (user_choice == 2 and num == 1):
            print(f"You lost: {choices[user_choice]} vs {choices[num]}")
        else:
            print(f"You won: {choices[user_choice]} vs {choices[num]}")
    else:
        print("Invalid input. Please enter a number between 1 and 3.")