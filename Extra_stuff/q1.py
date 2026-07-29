n=int(input("Enter a number which is a multiple of 4 :"))
result=0
if n%4==0:
    result = sum(1 / i for i in range(4, n + 1, 4))
    print("Sum of fractional sequence:", result)
else:
    print("Give input as a multiple of 4")
