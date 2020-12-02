#program to test divisibility of number with another number
n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
r = n1 % n2
if r == 0:
    print (n1 , "is divisible by " , n2)
else :
    print (n1 , "is not divisible by " , n2)
