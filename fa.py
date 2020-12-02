#prg to find area of triangle 
a = int (input("Enter the first side length :"))
b = int (input("Enter the second side length :"))
c = int (input("Enter the third side length :"))

s=(a+b+c)/2
 
area  = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print ("The area of the triangle is :" , round (area ,2))
