def my_dicount(price, discount):
	discount = price * (discount * 0.01)
	new_price = price - discount
	
	return new_price


print(my_dicount(150, 15))



