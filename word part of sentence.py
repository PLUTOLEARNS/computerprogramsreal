'''prgm to check whether any word is a part of sentence or not '''
line = input ("Enter any statement :")
word = input ("Enter the word : " )
if word in line :
    print ("Yes , " , word , "is part of" , line)
else:
    print ("No , " , word , "is not a part of" , line)
