def num(n):
    if n == 0:
        return
    print(n, end=" ")
    num(n-1)
n = int(input())
num(n)
