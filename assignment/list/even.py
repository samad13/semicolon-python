def even(arrays):
	another_array =[]
	for number in arrays:
		if(number %2 == 0):
			another_array.append(number)
	return another_array
		
print(even([4,5,6,7,8,9,10])) 
