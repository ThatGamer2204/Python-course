class Usa:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("Developed Country")

class India:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing Country")


obj_ind=India()
obj_usa=Usa()

for a in (obj_ind,obj_usa):
    a.capital()
    a.language()
    a.type()