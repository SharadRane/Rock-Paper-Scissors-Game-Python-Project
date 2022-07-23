
import random

print("STONE PAPER SCISSOR GAME")
print("GAME STARTS!!!")

def game(comp,you):

    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #Check all possibilities when computer choice 's'
    elif comp =='s':
        if you == 'p':
            return True

        elif you == 'sc':
            return False

    #Check all possibilities when computer choice 'sc'
    elif comp =='sc':
        if you == 's':
            return True

        elif you == 'p':
            return False

    #Check all possibilities when computer choice 'p'
    elif comp =='p':
        if you == 'sc':
            return True

        elif you == 's':
            return False


print("Computer turn: Stone(s) Paper(p) or Scissor(sc)\n ")
randNo=random.randint(1,3)
if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = 'p'

elif randNo == 3:
    comp = 'sc'

#Your Selection
you=input("Your Turn: Stone(s) Paper(p) or Scissor(sc): ")
a=game(comp,you)

print(f"Computer choice:\n{comp}")
print(f"Your choice:\n{you}")

if a==None:
    print("GAME IS TIE!!!")

elif a:
    print("YOU WON!!!")

else:
    print("YOU LOSE!!!")
    print("Better Luck next time....")


print("\nTHANK YOU!!!!\n\t For Playing Game....")