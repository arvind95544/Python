import random
var=10;
vary=0
varc=0
while(True):
    print(" 1. Snake\n","2. Water\n","3. Gun")
    var1=input("Select One item")
    if var1=='1':
        print("You choose :Snake")
    elif var1=='2':
        print("You choose :Water")
    else:
        print("You choose :Gun")
    lst= ["Snake","Water","Gun"]
    choice=random.choice(lst)
    print("Compurer choose :",end="")
    print(choice)
    if var1=='1' and choice=='snake':
        print("Match tai")
    elif var1=='1' and choice=='Water':
        print("You win!")
        vary=vary+1
    elif var1=='1' and choice=='Gun':
        print("You loss!")
        varc=varc+1
    elif var1=='2' and choice=='Snake':
        print("You loss!")
        varc = varc + 1
    elif var1=='2' and choice=='Water':
        print("Match tai")
    elif var1 == '2' and choice == 'Gun':
        print("You win")
        vary = vary + 1
    elif var1 == '3' and choice == 'Snake':
        print("You win")
        vary = vary + 1
    elif var1 == '3' and choice == 'Water':
        print("You loss!")
        varc = varc + 1
    elif var1 == '3' and choice == 'Gun':
        print("Match tai")
    var=var-1
    if var==0:
        print("GAME OVER !")
        break
    else:
        continue

if vary>varc:
    print("FINALY YOU WIN !")
elif vary==varc:
    print("Finaly MATCH TAI !")
else:
    print("FINALY YOU LOSS !")
