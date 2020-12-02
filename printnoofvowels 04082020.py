'''program to input a string and count the number of vowels.'''
#method 1
'''str = input ("Enter the string : ")
co = 0
for s in str : 
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        co += 1
print ("Total vowels found in this string is : " , co)'''

#method 2
str1 = input ("Enter the string : ")
vo = ['a','e','i','o','u','A','E','I','O','U']
cou = 0
for s in str1 :
    if s in vo:
        cou += 1
print ("Total vowels in the string : " , cou)

