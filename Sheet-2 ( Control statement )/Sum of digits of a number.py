a = int(input("Enter number: "))
tot = 0
temp = a
while temp > 0:
    digit = temp % 10
    tot += digit
    temp //= 10
print("Sum of digits =", tot)
