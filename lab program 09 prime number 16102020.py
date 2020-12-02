'''pgm 09 to find prime numnber or not'''
def dr():
    print("**********************************************")

dr()
print("Program 09 : To find whether the entered number is prime or not.")
dr()


n = int(input("Enter the number : "))

for i in range (2,n):
    if (n % i) == 0 :
        print (n , " is not a prime number.")
        break
else:
        print (n , " is a prime number.")
