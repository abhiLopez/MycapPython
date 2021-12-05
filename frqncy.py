#Program to print frequency of a string in decreasing order using fnctn and dict
a= input("Please enter a string: ")
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
#d.sort(reverse=True)
print (most_frequent(a),end=" ")



###########
# Another method 
from collections import Counter
test_str =input("Enter a String : ")  
res = Counter(test_str)
print ("Count of all characters in ",test_str," is :\n "+  str(res),end=" ")
