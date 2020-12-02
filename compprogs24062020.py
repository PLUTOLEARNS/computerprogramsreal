a=b=c=0
for i in range(1,2) :
    a = int(input("Enter Number 1 : "))
    b = int(input("Enter Number 2 : "))
    if b == 0:
        print("Division by zero error !!")
        continue
    else :
        c = a//b
        print("Quotient = " , c)
        