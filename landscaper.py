money = 0
hasScissors = False
hasLawnMower = False

while(True):
    
    user_choice = input("[1] Cut Lawns with Teeth [2] Buy Scissors ($5) [3] Cut Lawns with Scissors [4] Buy Push Lawnmower ($25) [5] Cut Lawns with Push Lawnmower  [10] Check Money ")
    
    if (user_choice == "1"):
        money += 1
        
        print(f"You cut lawns with your teeth and earned $1! Total money: ${money}\n")
        
    if (user_choice == "2"):
        # check if user already has scissors
        if (hasScissors == True):
            print("You already have scissors.\n")
        # check if user has enough money
        elif (money >= 5):
            money -= 5             # subtract scissor cost
            hasScissors = True     # user has scissors now
            print("You bought a pair of scissors! Now you can cut lawns with them.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
    
    if (user_choice == "3"):
        # check if user has scissors
        if (hasScissors == True):
            money += 5
            print(f"You cut lawns with scissors and earned $5! Total money: ${money}\n")
        else:
            print("You don't have scissors yet. Buy a pair first!\n")
            
    if (user_choice == "4"):
        # check if user alread has lawnmower
        if (hasLawnMower == True):
            print("You already have a push lawnmower.\n")
        # check if user has enough money
        elif (money >= 25):
            money -= 25
            hasLawnMower = True
            print("You bought a push lawnmower! Now you can cut lawns with it.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
            
    if (user_choice == "5"):
        # check if user has lawnmower
        if (hasLawnMower == True):
            money += 50
            print(f"You cut lawns with the push lawnmower and earned $50! Total money: ${money}")
        else:
            print("You don't have a push lawnmower yet. Buy one first!\n")
            
    if (user_choice == "10"):
        print(f"Total money: ${money}")