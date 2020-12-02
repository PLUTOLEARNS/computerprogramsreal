'''pgm 19 ascii code'''
def dr():
    print("**********************************************")

dr()
print ("Program 19 : To print the ASCII values.")
dr()
var = True
while var:
    choice = int(input("1. Enter 1 to get the ordinal value of a Character\n 2. Enter 2 to find Character from the Ordinal Value  : "))
    if choice == 1:
        ch = input("Enter a character : ")
        print (ord(ch))
    elif choice == 2:
        val = int(input("Enter an integer value : "))
        print (chr(val))
    else :
        print("You have entered a wrong choice!")
        break
    option = input("Do you want to continue ? Y / N : ")
    if option == 'y' or option == 'Y':
        var = True
    else:
        var = False
    
