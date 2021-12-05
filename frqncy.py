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

from collections import Counter
  
# initializing string 
test_str =input("Enter a String : ") 
  
# using collections.Counter() to get 
# count of each element in string 
res = Counter(test_str)
  
# printing result 
print ("Count of all characters in ",test_str," is :\n "+  str(res),end=" ")
