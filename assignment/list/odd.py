def odd(arrays):
	another_array =[]
	for number in range(len(arrays)):
		if(number %2 != 0):
			another_array.append(arrays[number])
	return another_array
		
print(odd([4,5,6,7,8,9,10])) 




