n = int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print("_",end="")
    for q in range(n-i):
        print("* ",end="")
    print()
