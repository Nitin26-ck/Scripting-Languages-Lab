"""
Write a python program to create a class ‘Rectangle’.
This class should include a constructor to initialize the dimensions. 
Include a function in the class to compute the area of the rectangle.
Create objects of the class and print area.
"""

class Rectangle:
	def __init__(self):
		self.l = int(input("Enter length"))
		self.b = int(input("Enter breadth"))
	def area(self):
		print("The area of the given rectangle is",self.l*self.b)

R=Rectangle()
R.area()
