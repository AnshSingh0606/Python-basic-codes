a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a >= b and a >= c:
    print("max:", a)
elif b >= a and b >= c:
    print("max:", b)
else:
    print("max:", c)

