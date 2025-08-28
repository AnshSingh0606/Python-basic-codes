n = int(input("enter number:"))
for i in range(n):
    for j in range(n-i):
        print("_",end="")
    for q in range(i+1):
        print("* ",end="")
    print()

