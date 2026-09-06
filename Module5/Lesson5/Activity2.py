from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run.")

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Dog(Animal):
    def move(self):
        print("I can bark.")

class Lion(Animal):
    def move(self):
        print("I can roar.")

Alson=Snake()
Saket=Dog()
Anshuman=Lion()
Mithran=Human()
Alson.move()
Anshuman.move()
Saket.move()
Mithran.move()