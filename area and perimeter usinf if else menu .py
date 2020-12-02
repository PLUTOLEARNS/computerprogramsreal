#prg to display a menu to calculate area and perimeter of a circle

r = float(input("Enter the radius : "))
print ("1.Calculate the area of circle")
print ("2.Calculate the perimeter of circle")
ch = int(input("Enter your choice , 1 or 2 : " ))
if ch == 1:
    ar = 3.14 *r*r
    print ("The area of the circle is : " , ar)
else :
    pr = 2*3.14*r
    print("Perimeter of circle is : " , pr)
