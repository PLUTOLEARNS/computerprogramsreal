"""write a program to display all the city names from a list which are starting with the letter 'A' """
inp = eval(input("Input the cities : "))
for ci in inp:
    if ci[0] == "A":
        print(ci)
    break
else:
    print("No such city with starting letter A found.")