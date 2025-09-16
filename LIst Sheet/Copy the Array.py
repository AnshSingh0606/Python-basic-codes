A = list(map(int,input("Enter list: ").split()))
B = int(input("Enter a number: "))
sum = []
for i in A:
    sum = sum + [i + B]
print(sum)
         