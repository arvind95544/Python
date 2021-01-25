n=21
i=1
print("Guess any number which belongs between 0 to 50\n","You have only 5 choice")
while(True):
    var1=int(input("Enter Number\n"))
    if var1==21:
        print("You won : Number is 21")
        print("You have done in",i,"guess")
        break
    else:
        if i==5:
            print("Game over!")
            break
        print("Wrong number","You have only",5-i,"chance")
        if var1>21:
         print("Number is grater than actual number")
        else:
         print("Number is lasser than actual nuber")
        i=i+1
        if i<=5:
             continue
        else:
            break

    continue

