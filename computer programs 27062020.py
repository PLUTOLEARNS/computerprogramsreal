"""program to print the elements of a tuple('hello','python','programming ) in seperate lines and display their indexes voth backwards and forwards"""
"""t = ('hello','python','programming')
le = len(t)
for a in range(le):
    print("at indexes " , a, "and", (a-le) ,"element : " , t[a])"""
a=4

b= ''

while a >0:

    for i in range(a,0,-1):
        b += str(i)

print(b)

a -= 1

b = ""