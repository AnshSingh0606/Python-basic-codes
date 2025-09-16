a = list(map(int,(input().split())))
b = []
for i in range(1,len(a)+1):
    b = b + [a[-i]]
print(b)