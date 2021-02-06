"""
Create a list of 6 numbers.
Use ‘list-comprehension’ to create a new list where each element in the original list is multiplied by 3.
Use ‘lambda’ and ‘reduce’ function to find the sum of the elements of the original list as well as the new list.
"""

from functools import reduce
mylist=[1,2,3,4,5,6]
print("Original",mylist)
newlist=[x*3 for x in mylist]
print("New",newlist)
or_sum = reduce(lambda x,y: x+y,mylist)
print("Original sum",or_sum)
new_sum = reduce(lambda x,y: x+y,newlist)
print("New sum",new_sum)

