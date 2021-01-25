def feb_1(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        feb=feb_1(n-1)+feb_1(n-2)
        return feb
print(feb_1(int(input("Enter number"))))
