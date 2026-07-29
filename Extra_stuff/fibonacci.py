n=int(input("Enter nth term :"))
x=n-2
lst=[0,1]
if x==0:
    lst=[0,1]
    print(f"Sequence of Fibonacci series till {n} terms is : {lst}")
elif x==-1:
        lst=[0]
        print(f"Sequence of Fibonacci series till {n} terms is : {lst}")
elif x<-1:
    print("Invalid n, please enter a whole number.")
else:
     for i in range(1,x+1):
          lst.append(lst[-1]+lst[-2])
     print(f"Sequence of Fibonacci series till {n} terms is : {lst}")