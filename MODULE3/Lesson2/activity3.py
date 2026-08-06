x=int(input("Enter positive number :"))
def factorial(x):
    """The factorial function does a factorial of a number which is defined as the number multiplied by all preceeding natural numbers."""
    if x==1 or x==0:
        f=1
    else:
        f=x
        f*=factorial(x-1)
    return f
print(factorial.__doc__)
print(f"Factorial of {x} is {factorial(x)}.")
