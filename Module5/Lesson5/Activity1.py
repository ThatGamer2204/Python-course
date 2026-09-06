from abc import ABC,abstractmethod
class Absclass(ABC):
    
    def print(self,x):
        self.x=x
        print(self.x)
    @abstractmethod
    def task(self):
        pass
class test_class(Absclass):
    def task(self):
        print("This is a child class.")


test_obj=test_class()
test_obj.task()
test_obj.print(5)