import random as r

def gameWin(comp,you):

    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's': 
        if you == 'r':
            return True
        elif you == 'p':
            return False

randNo = r.randint(1,3)

print(''' ****Welcome to ROCK SCISSORS PAPER game****
    Computer chose between rock scissor or paper.
            Now its your turn.\n''')

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

#Allow user to enter their choice

you = input("Press s for scissor, r for rock and p for paper")


if gameWin(comp,you) == None:
    print ("Its a tie.")
elif gameWin(comp,you) == True:
    print("Congratulations! You won")
elif gameWin(comp,you) == False:
    print("Computer won.")

#Printing computer choice

print (f"Computer choose {comp}")


