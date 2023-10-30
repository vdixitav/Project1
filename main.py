
#Snake water gun / Rock paper scissor


import random

def gameWin(comp ,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True 
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True        



print("Comp Turn : Snake(s) Water(w) Or Gun(g) ?")
randNO=random.randint(1,3)
print(randNO)

if randNO==1:
    comp ='s'
elif randNO==2:
    comp ='w' 
elif randNO==3:
    comp ='g'        

you=input("Your Turn : Snake(1) Water(2) Or Gun(3) ?")

a=gameWin(comp,you)

print(f"Computer chose{comp}")
print(f"You chose{you}")

if a==None:
    print("the game is tie!")
elif a:
    print('You win!') 
else:
    print('You loss!')        

