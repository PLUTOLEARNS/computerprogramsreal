"""bonus = 0
sale = int(input("Enter Monthly Sales :"))
if sale >50000:
    bonus = sale * 10 /100
print("Bonus = " + str(bonus))
t = bonus + sale
print ("Monthly Salary with bonus = " , t)"""
n = int(input ("Enter any number : "))
for i in range(1,31):
    print(n," X " , i , " = " , n*i)

"""program to print the elements of a tuple('hello','python','programming ) in seperate lines and display their indexes voth backwards and forwards"""
t = ('hello','python','programming')
le = len(t)
for a in range(le):
    print("at indexes " , a, "and", (a-le) ,"element : " , [a])