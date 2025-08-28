n = int(input("enter number:"))
for i in range(n):
    print("*",end="")
    for j in range(n-i):
        print("_",end="")
    print("*",end="")
    print()

