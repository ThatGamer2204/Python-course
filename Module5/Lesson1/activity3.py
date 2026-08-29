class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=Parrot("Harry",17)
woo=Parrot("Peter",17)

print(blu.name,blu.age,blu.species)
print(woo.name,woo.age,woo.species)