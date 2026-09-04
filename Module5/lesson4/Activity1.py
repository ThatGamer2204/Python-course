class myClass:
    __privateVar=27
    def __privMeth(self):
        print("This is a private method")
    def hello(self):
        print(self.__privateVar,myClass.__privateVar)

foo=myClass()
foo.hello()
foo.__privMeth()