import math
def divide_or_sqaure(number):
	division = number / 5
	square_root = math.sqrt(number)
	if (number % 5 == 0):
		return f"{square_root:.2f}"
	else: 	
		return division

print(divide_or_sqaure(10))



