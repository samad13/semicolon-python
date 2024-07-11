
pick = 0
account = 0
while(pick != -1):
	pick = int(input("press 1 to deposit, press 2 to withdraw and -1 to see your balance: "))
	if(pick == 1):
		deposit = int(input("deposit: "))
		account += deposit  
	elif(pick == 2):
		withdraw = int(input("withdraw: "))
		account -= withdraw 
	
 
print(account)