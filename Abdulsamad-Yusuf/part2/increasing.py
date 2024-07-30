def increasing(num1,num2,num3):
	largest = "none"
	if (num1 >= num2 and num1 >= num3 ):
		largest = num1
	elif(num2 >= num3 and num2 >= num3 ):
		largest = num2
	elif(num3 >= num1 and num3 >= num2 ):
		largest = num2

	return largest	

print(increasing(4,5,3))