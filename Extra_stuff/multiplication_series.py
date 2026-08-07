a=1
b=3
sum=0
lst=[]
for i in range(1,11):
    if i ==1:
        print(i)
        lst.append(i)
    else:
        a+=2
        b+=2
        print(a*b)
        lst.append(a*b)
print(lst)
for i in lst:
    sum+=i
print(sum)