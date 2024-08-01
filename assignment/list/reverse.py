def reverse(array):
	thelength = len(array)
	reversed_array = []

	for number in range(thelength-1,-1, -1):
		reversed_array.append(array[number])
		
	return  reversed_array 




print(reverse([4,5,6,7,8,9,10])) 


