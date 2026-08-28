set1={"Apple","banana","Orange","mango"}
set2={"Peach","Cherry","Pineapple","Watermelon"}
set1.add("Cherry")
print(set1.intersection(set2))
from array import array
fruit_counts=array('i',[12,78,347,279,1])
fruit_counts.insert(2,23)
fruit_counts.append(279)
print(fruit_counts.count(279))
fruit_counts.reverse()
print(fruit_counts)
fruitsorted=array('i',sorted(fruit_counts))
print(fruitsorted)