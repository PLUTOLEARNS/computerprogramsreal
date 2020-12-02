# Python program to find sum of elements in list 
'''s = 0
l = eval(input("Enter the list : "))
le = len(l)
for i in range(0,le): 
    s = s + l[i] 
print("Sum of the elements in given list: ",s) '''
lst = eval(input("Enter the list : ")
i = 0
s = 0
while(i<len(lst)):
    if lst[i]%2 != 0:
        s = s + lst [i]
    i += 1
print("The sum is : " , s)
