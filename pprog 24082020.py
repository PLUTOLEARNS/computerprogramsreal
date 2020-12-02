lst = eval(input("Enter the list : "))
length = len(lst)
bi = sb = lst[0]
for i in range (1,length):
    if lst[i]>bi:
           sb = bi
           bi = lst[i]
    elif lst[i]>sb:
        sb = lst[i]
print ("Largest number  : " , bi )
print (" Second largest number :" , sb)
