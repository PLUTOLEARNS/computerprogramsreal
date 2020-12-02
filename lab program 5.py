"""5.Program to display the area or perimeter of circle"""
r = float(input("Enter the radius of the circle : "))
print ("1. Calculate area. ")
print("2. Calculate the perimeter. ")
print("3. Calculate both.")
c = int(input("Enter your choice : "))
if c == 1:
    ar = 3.14 * r * r
    print ("The area of the circle is : ", ar)
elif c == 2 :
    per = 2 * 3.14 * r
    print("The perimeter of the circle is : " , per)
else :
    ar = 3.14 * r * r
    per = 2 * 3.14 * r
    print ("The area of the cirlce is : " , ar , "and" , "the perimeter is : " , per)




