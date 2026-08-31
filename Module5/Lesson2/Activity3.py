tuplex=(10,20,30,40,50,60,70)
sum=int(input("Enter the desired sum :"))
class Paired_elements:
    def twosum(self,tuplex,sum):
        dic={}
        for i,item in enumerate(tuplex):
            if (sum-item) not in dic:
                dic[item]=i
            else:
                print(dic)
                return (i, dic[sum-item])

pair_elements1=Paired_elements()
index1,index2=pair_elements1.twosum(tuplex,sum)
print("The pair is at index :",index1,index2)  