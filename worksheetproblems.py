names  = ["allahabad" , "Lucknow" , "varanasi" , "kanpur" , "agra" , "ghaziabad" , "mathura" , "meerut"]
city = input ("Enter city to search : ")
for c in names :
    if c == city:
        print ("City Found")
        break
    else:
        print("City not found")
