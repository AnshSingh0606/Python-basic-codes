a = int(input("Enter angle a: "))
b = int(input("Enter angle b: "))
c = int(input("Enter angle c: "))

if a + b + c == 180:
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Not a valid triangle")

