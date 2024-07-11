number = int(input("input number: "))
#number= int(input("enter your first name: "))

if(number >= 75 and number <= 100):
	print("A")
elif(number >= 65 and number <= 74):
	print("B")
elif(number >= 50 and number <=64 ):
	print("C")
elif(number >= 40 and number <= 49):
	print("D")
elif(number <= 39):
	print("F")
else: 
	print("number beyond 100, so not allowed")
