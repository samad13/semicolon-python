from random import randint

number = randint(1,1000)
count = 0
do_again = ""
while(do_again != "no" ):
	answer = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
	count +=1
	if(answer > number):
		print("Too high.. Try again")
	elif(answer < number):
		print("Too low.. Try again")
	elif(number == answer):	
		if (count <= 10):
			print(f"Congratulations. You guessed the number in {count} times!")
		elif(count > 10):
			print(f"Congratulations. You guessed the number in {count} times, you can do better next time!")
		number = randint(1,10)
		count -=count
		do_again = input("input no  to stop or yes to continue: ")