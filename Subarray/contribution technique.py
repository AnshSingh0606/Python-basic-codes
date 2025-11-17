n = int(input("enter n: "))
a = list(map(int, input().split()))
t = 0
for i in range(n):
    t =t + a[i]*(i+1)*(n-i)
print(t)
