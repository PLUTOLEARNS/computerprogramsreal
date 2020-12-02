"""2. Program to swap two numbers without using third variable."""
"""a = a + b
b = a - b
a=a-b"""
a = int(input("Enter the value of Number 1 : "))
b = int(input("Enter the value of Number 2 : "))
print ("Number before swapping " , a,b)
a = a+b
b = a-b
a= a-b
print("Numbers after swapping is : " ,a,b)
"""Flowchart:
start 
input number 1 , assign to variable a
input number 2 , assign variable b 
a = a + b
b = a - b
a = a - b
display a and b"""