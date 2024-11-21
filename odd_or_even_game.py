import random
inputs = [1,2,3,4,5,6,10]
def userBat(k,pr):
    runs = 0
    out = 0
    while out == 0:
        user_choice = int(input("\nEnter your choice[1-6 or 10]: "))
        pc_choice = random.choice(inputs)
        print("PC's coice: ",pc_choice)
        if user_choice == pc_choice:
            print("OUT")
            out = 1
            print("Final Total: ",runs)
        else:
            runs += user_choice
            print("Your current runs: ",runs)
            if k == 0 and runs < pr:
                print("Required: ",(pr - runs) + 1)
        if k == 0 and runs > pr:
            out = 1
    return runs

def pcBat(k,ur):
    runs = 0
    out = 0
    while out == 0:
        user_choice = int(input("\nEnter your choice[1-6 or 10]: "))
        pc_choice = random.choice(inputs)
        print("PC's Choice: ",pc_choice)
        if user_choice == pc_choice:
            print("OUT")
            out = 1
            print("Final Total: ",runs)
        else:
            runs += pc_choice
            print("PC's current runs: ",runs)
            if k == 1 and runs < ur:
                print("Required: ",(ur - runs) + 1)
        if k == 1 and runs > ur:
            out = 1
    return runs

play = 'Y'
while play == 'Y':
    choice = input("Odd or Even: ")
    user_toss = int(input("Enter your choice[1-6 or 10]: "))
    pc_toss = random.choice(inputs)
    print("PC's Choice: ",pc_toss)
    print()
    total = user_toss + pc_toss
    if choice == 'Even' or choice == 'even':
        if total % 2 == 0:
            print("You won the toss")
            k = input("Do you wanna bat or bowl? ")
            if k == 'bat':
                user_bat = 1
            else:
                user_bat = 0
        else:
            print("PC won the toss")
            user_bat = random.randint(0,1)
            if user_bat == 1:
                print("PC chose to bowl first")
            else:
                print("PC chose to bat first")    
    else:
        if total % 2 ==0:
            print("PC won the toss")
            user_bat = random.randint(0,1)
            if user_bat == 1:
                print("PC chose to bowl first")
            else:
                print("PC chose to bat first")
        else:
            print("You won the toss")
            k = input("Do you wanna bat or bowl? ")
            if k == 'bat':
                user_bat = 1
            else:
                user_bat = 0
    user_runs = 0
    pc_runs = 0
    if user_bat == 1:
        print("\n\nYour Batting")
        user_runs = userBat(user_bat,pc_runs)
        print("\n\nTarget: ",user_runs+1)
        print("\n\nPC's Batting")
        pc_runs = pcBat(user_bat,user_runs)   
    else:
        print("\n\nPC's Batting")
        pc_runs = pcBat(user_bat,user_runs)
        print("\n\nTarget: ",pc_runs+1)
        print("\n\nYour Batting")
        user_runs = userBat(user_bat,pc_runs)
    print()
    print("Your Total Runs: ",user_runs)
    print("PC's Total Runs: ",pc_runs)
    if pc_runs > user_runs:
        if user_bat == 0:
            print(f'PC Won by {pc_runs - user_runs} runs')
        else:
            print("PC Won by 1 wicket")
        play = 'N'
    elif pc_runs < user_runs:
        if user_bat == 1:
            print(f'\nYou Won by {user_runs - pc_runs} runs')
        else:
            print("You Won by 1 wicket")
        play = 'N'
    else:
        print("Tie")
        play = input("Rematch?(Y/N) ")
print()

