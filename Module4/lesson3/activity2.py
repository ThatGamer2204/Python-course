test_dic={"word":2,"saket":22,"rocket":12,"Sonic":31,"groot":34}
print(test_dic)
k=2
res=0
for i in test_dic:
    if test_dic[i]==k:
        res+=1
print("the frequency of 2 in test_dic is",res)