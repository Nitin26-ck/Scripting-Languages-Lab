"""Introduction to Python:
​Write Python programs to do the following: 
a) Read a list of elements. Create a new list having all the elements minus the duplicates (Use functions).
Use one-line comprehensions to create a new list of even numbers.
Create another list reversing the elements.
"""

S = [x**2 for x in range(10)] # read elements  to list
M = [x for x in S if x % 2 == 0]
M.reverse()
print(M)
