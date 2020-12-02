"""4.Program to accept 3 numbers and print the largest number using only if statements."""
x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))
z = float(input("Enter the third number : "))
m = x
if y > m:
    m = y
if z > m:
    m = z
print ("Largest number is : " , m)
"""start 
input variables 
max = x
if max < y 
yes : max = y
no : max = x
if max < z
yes : max = z
no : max = y"""

