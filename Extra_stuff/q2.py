n = int(input("Enter multiple of 10 :"))
sign=1
if n%10==0:
    result = 0
    for i in range(1, n + 1, 10):
        result=(i*sign)+result
        sign*=-1
    print("Sum of alternating sequence:", result)
else:
    print("Enter a multiple of 10!!")