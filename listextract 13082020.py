"""Extract two list out of given list display and print the sum append function will add the content or element to the end of list if the index number is not specified"""
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
s = ls[5:15:2]
s1 = ls[::4]
sum1 = avg = 0
print("Sublist 1")
for a in s:
    sum1 = sum1 + a
    print(a , end = " ")
print()
print("Sum of elements of Sublist 1 : ", sum1)
print("Sublist 2")
sum1 = 0
for a in s1 :
    sum1 += a
    print(a , end = " ")
print()
a = sum1 / len(s1)
print("Average of elements of Sublist 2 is " , a)