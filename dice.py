import random
while True:
    play = input("Roll the dice to Play:(y/n) ").lower()
    if play == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        
        print(f'({die1},{die2})')
        if die1==die2:
           print("YOU got the Point")
    elif play == 'n':
        print("Thank You for  playing") 
        break
    else:
        Print("Invalid choice You used")       