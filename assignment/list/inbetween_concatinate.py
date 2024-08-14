def inbetween_concatinate(a,b):
	max=len(a) +  len(b)
	another=[]
	counta = 0
	countb = 0
	for number in range(max):
		if(number%2==0):
			another.append(a[counta])
			counta+=1
		elif(number%2!=0):
			another.append(b[countb])
			countb+=1	
	return another 
print(inbetween_concatinate(["a","b","c"],[1,2,3])) 

