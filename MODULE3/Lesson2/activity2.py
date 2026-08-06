num=int(input("Enter number :"))
def cube(num):
    return num**3

def by_three(num):
    if num%3==0:
        c=cube(num)
    else:
        c=False
    return c
print(by_three(num))


