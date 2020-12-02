'''pgm to read string and display it in reverse order-display on character line'''
st = input ("Enter the  string : ")
print(st, "in reverse order is : ")
ln = len(st)
for a in range (-1 , (-ln-1), -1):
    print(st[a])