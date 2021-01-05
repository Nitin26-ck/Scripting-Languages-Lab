#Write a python program to read in a list of numbers.
#Use one-line comprehensions of create a new list of even numbers.
#Create another list reversing the elements.
S = [x**2 for x in range(10)] # read elements  to list
M = [x for x in S if x % 2 == 0]
M.reverse()
print(M)