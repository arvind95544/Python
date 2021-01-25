print("Enter first ")
num1=input()
print("Enter second number")
num2=input()

try:
    num3 = int(num1) + int(num2)
    print("Sum of these two number is : ",num3)
except Exception as e:
    print(e)
print("This is important line")