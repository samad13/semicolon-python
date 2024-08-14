def forlup(arrays):
	total = 0
	for number in arrays:
        	total+=number
   
	return total
print(forlup([1,2,3,4])) 


def whilelup(arrays):
	total = 0
	number = 0
	while number < len(arrays):
		total+=arrays[number]
		number+=1
	return total
print(whilelup([1,2,3,4])) 
