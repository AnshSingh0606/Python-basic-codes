a = list(map(int,(input().split())))
even = []
odd = []
for i in a:
    if i%2==0:
        even = even + [i]
    else:
        odd = odd + [i]
print(even)
print(odd)
