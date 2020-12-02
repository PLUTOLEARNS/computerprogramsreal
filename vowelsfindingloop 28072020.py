#python program to count vowels in string
st = input ("Enter the string : ")
v = 0
for i in st :
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ) :
        v += 1
print ("The numbers of vowels in the string is : " , v)