def only_float(a, b):
	if(type(a) == float and type(b) ==float):
		return 2
	elif(type(a) == float or type(b) ==float):
		return 1
	elif(type(a) != float and type(b) !=float):
		return 0


print(only_float(21, 2))