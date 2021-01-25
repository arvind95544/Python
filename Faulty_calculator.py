#Faulty calculator which is correct for all calculation except 55+7=77,45*3=55,56/6=4


print("Enter first number")
var1=int(input())
print("Please select : +,-,*,/")
var2=(input())
print("Enter Second number")
var3=int(input())
if var2=="+":
    if var1==56 and var3==9:
        print("77")
    else:
        print(var1+var3)
elif var2=="-":
    print(var1-var3)
elif var2=="*":
    if var1==45 and var3==3:
        print("555")
    else:
        print(var1*var3)
elif var2=="/":
    if var1==56 and var3==6:
      print("4")
    else:
        print(var1/var3)

