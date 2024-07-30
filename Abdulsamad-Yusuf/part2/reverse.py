def reverse(number):

	reversnum = 0
	while(number > 0):
		
		reversnum   = (reversnum * 10) + (number % 10)
		
		number = number // 10
	
	return reversnum

#print(reverse(121))

def palindrome(number):
	
	if (reverse(number) == number):
		return True
	else:
		return False


#reverse(121)
print(palindrome(6542))