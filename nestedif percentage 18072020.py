pt = float(input("Enter your percentage :"))
if 90 <= pt < 100:
    print("Your grade is : A+.")
if 80 <= pt < 90:
    print("Your grade is : A.")
if 60 <= pt < 80:
    print("Your grade is : B.")
else:
    if pt < 60:
        print("You have failed!")