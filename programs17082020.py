'''program to calculate the mean of the given list of numbers'''
l = eval(input("Enter the list : "))
ln = len(l)
m = s = 0
for i in range(0,ln):
    s += l[i]
m = s/ln
print ("The given list is : " , l)
print ("The mean of the given list : " , m)
print("The sum of the given list : " , s)
