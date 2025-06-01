import random

minimunRange=int(input('enter the starting range'))
maximumRange=int(input('enter the maximum range'))
computerChoice=random.randint(minimunRange,maximumRange)

userChoice=int(input('enter the your choice'))

chance=2

while chance>0:
    if(computerChoice==userChoice):
        if(chance==3):
            print("perfect")
            break
        elif(chance==2):
            print('good')
            break
        else:
            print('correct nice try')
            break
    
    else:
        if abs(userChoice - computerChoice) > (maximumRange / 3):
            print('you are too away from the right one')
            userChoice=int(input('try one more time'))
        else:
            print("close")
            userChoice=int(input('try one more time'))
        chance-= 1

        if chance == 0:
            print(f"Sorry, you've used all chances. The correct number was {computerChoice}.")





