def findlargestelement(array):
	largest = array[0]
	for number in array:
		if(number > largest):
			largest = number
          
	return largest
    


print(findlargestelement([3,5,7,8,0,19]))
