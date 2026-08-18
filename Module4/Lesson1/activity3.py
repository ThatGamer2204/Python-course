L=[1,3,5,2,34,35,4,12]
count=0
print(L)
for i in L:
    count+=i
avg=count/len(L)
print(count,",",avg)
L.sort()
print(L[0],",",L[-1])
