price = int(input("what is the price of the car: "))

if(price <= 1000000):
	print("tax is : ", price * 0.1);
elif(price >= 1000000 and price <= 3000000 ):
	print("tax is : ", price * 0.15)
elif(price > 3000000 and price < 5000000 ):
	print("tax is : ", price * 0.2)
elif(price >= 5000000 ):
	print("tax is : ", price * 0.25)






