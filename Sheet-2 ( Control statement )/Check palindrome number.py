a = int(input("Enter number: "))
temp = a
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev == a:
    print("Palindrome")
else:
    print("Not palindrome")
