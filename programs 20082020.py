'''prg to search for an element in a given list of numbers '''
"""l = eval(input("Enter the list : "))
le = len(l)
e = eval(input("Enter the element to be searched : "))
for i in range(0,le):
    if e == l[i]:
        print(e, "found at index : " ,i)
        break
    else:
        print(e , "not found.")"""
#Second program
#program to find the minimum element from a list of elements along with its index
"""ls = eval(input("Enter the list : "))
lg = len(ls)
me = ls[0]
mi = 0
for i in range(1,lg):
    if ls[i] <= me:
        me = ls[i]
        mi = i
print("Given list is : ")
print("The minimum element of the list is : " , me , "at index" , mi)"""
###########program to count frequency of a given element in a list of numbers######################
lst = eval(input("Enter the list : "))
length = len(lst)
element = int(input("Enter the element : "))
count = 0
for i in range(0,length):
    if element == lst[i] :
        count+=1
if count ==0:
    print(element , "not found")
else:
    print(element , "has frequency as", count , "in given list.")
###### eval can be entered in the "element" variable to accept characters and digits both.#####