a = list(map(int,(input().split())))
c_odd = 0
c_even = 0
for i in a:
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
dif = c_even-c_odd
print(abs(dif))