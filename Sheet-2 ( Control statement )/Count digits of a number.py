a = int(input("Enter number: "))
b_count =0
c = a
while c > 0:
    b_count += 1
    c //= 10
print("NO. of digits =", b_count)
