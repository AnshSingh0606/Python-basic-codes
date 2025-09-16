a = list(map(int,input("Enter array: ")))
for i in range(len(a)):
    for j in range(i):
        if (a[i]>j):
            print("max: ", a[i])
        


