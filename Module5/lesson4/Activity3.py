class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
       return (f"{self.x},{self.y}")

point1=Point(2,3)
print(point1)