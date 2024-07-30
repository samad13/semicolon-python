for number in range (999, 3001):
	
	value1 = number // 1000
	value2 = number % 10
	placeholder2 = number // 10
	placeholder1 = number // 100
	value4 = placeholder2 % 10
	value3 = placeholder1 % 10

	if (value1 %2==0 or value2 % 2==0 or value3 % 2==0 or value4 % 2==0 ):
		print(f"{value1}{value2}{value3}{value4,}")
		





	