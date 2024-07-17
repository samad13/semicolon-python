price = int(input("what is the price of the car: "))

if(price < 1000000):
	print("your road tax is 10%")
elif(price >= 1000000 and price <= 3000000 ):
	print("your road tax is 15%")
elif(price > 3000000 and price < 5000000 ):
	print("your road tax is 20%")
elif(price >= 5000000 ):
	print("your road tax is 25%")






