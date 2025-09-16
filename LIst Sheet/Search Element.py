a = list(map(int,input().split()))
b = int(input())
count = 0
for i in range(len(a)):
    if (a[i]==b):
        count = count+1
print(count,"times")
