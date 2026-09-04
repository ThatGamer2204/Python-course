class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"The current selling price is {self.__maxprice}.")

    def setmaxprice(self,price):
        self.__maxprice=price

c=Computer()
c.setmaxprice(1000)
c.sell()

