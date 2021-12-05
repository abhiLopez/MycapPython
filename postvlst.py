#4:Program to print a-Positive list of numbers from given list of integers
l=list(map(int,input("Enter some comma seperated positive numbers: ").split(",")))
r=[x for x in l if x>0]
print("Positive list of numbers are: ",r)
