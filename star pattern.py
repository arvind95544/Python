#Acording to me we can't define star pattern
print("Enter number to get star pattern")
var1=int(input())
var2=int(input("Type 1 or 0"))
var3=bool(var2)
if var3==True:
    for x in range(var1):
       y=x+1
       for x in range(y):
          print("*",end="")
       print()
elif var3==False:
   for x in range(var1):
       y=var1-x
       for x in range(y):
          print("*",end="")
       print()