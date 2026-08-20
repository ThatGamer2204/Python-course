tuplex=(1,2,3,2,1)
n=-1
j=len(tuplex)-1
j1=0
flag=True
for i in tuplex:
    while j1<j:
        if i==tuplex[n]:
           n-=1
           j-=1
           j1+=1
           flag=True
        else:
            flag=False
            break
if flag==False:
    print("It is not a palindrome")
else:
    print("It is a palindrome")