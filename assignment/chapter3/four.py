sum = 0
product = 1
count = 0

number1 = int(input('put a number: '))

sum += number1
product *number1
count +=1
largest = number1
smallest = number1

for number in range(3):
	number1 = int(input('put a number: '))
	sum+= number1
	product*=number1
	
	count+=1
	
	largest = max(largest, number1)
	smallest = min(smallest,number1)
average = sum / count

print('sum', sum, 'product:', product, 'average:', average, 'largest:', largest, 'smallest', smallest)
#float('-inf')
#float('inf')