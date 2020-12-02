tm = input("What would you like to do? Convert temperature from  1) Fahrenheit to Celsius or 2) Celsius to Fahrenheit? : ")
tm2 = float(input("What is your number temperature to be converted ? : "))

if tm == '1':
	c = (tm2 - 32) * 5 / 9
	print("Temperature from Fahrenheit to Celsius is  : " , c , "ºC")
elif tm == '2':
	f = (tm2 * 9 / 5 + 32)
	print("Temperature from Celsius to Fahrenheit is : " , f ,"ºF")
else:
	print("Invalid input.")
