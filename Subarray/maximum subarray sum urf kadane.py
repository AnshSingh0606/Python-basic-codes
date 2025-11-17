n = int(input("enter n: "))
a = list(map(int, input().split()))
cs = a[0]
ms = a[0]
for i in range(1, n):
    cs = max(a[i], cs + a[i])
    ms = max(ms, cs)
print(ms)
