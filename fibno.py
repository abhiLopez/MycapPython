#3:Program to print fibonaci series of N terms
n=int(input("Enter the limit of fibonaci series: "))
a=c=d=0
b=1
print("Fibonaci series upto ",n," terms are: ")
while d<=n-1:
    print(c," ",end="")
    a=b
    b=c
    c=a+b
    d=d+1