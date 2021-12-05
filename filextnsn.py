#2:Program to print the extension of a filename entered by user
f=input("Enter the Filename: ")
x=f.split(".")
if x[-1]=='py':
    print("The extension of the file is: 'Python'")
else :
    print("The extension of the file is: ",x[-1])