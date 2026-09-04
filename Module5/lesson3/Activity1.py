class FamilyMember:
    def __init__(self,eyecolor,height):
        self.eyecolor=eyecolor
        self.height=height
    def showtraits(self):
        print(self.eyecolor,self.height)

class Kid(FamilyMember):
    def __init__(self,name,age, eyecolor, height):
        super().__init__(eyecolor, height)
        self.name=name
        self.age=age
    def showtraits(self):
        print(self.name,self.age)
        super().showtraits()
    def play(self):
        print(f"My name is {self.name}, I am playing Tennis!")



kid1=Kid("Saket",16,"Black",165)
kid1.showtraits(),kid1.play()