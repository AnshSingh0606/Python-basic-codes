n = int(input("enter n: "))
a = list(map(int, input().split()))
l, r = map(int, input().split())
l =l- 1
r = r- 1
s = 0
for i in range(l, r+1):
    s =s +a[i]
print(s)
