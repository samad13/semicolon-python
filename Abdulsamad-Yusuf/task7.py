#collect the number of month and save it
#declare final_accout_value
# delcare mothly_interest_rate 
# add 1 with mothly_interest_rate divide by final_accout_value and raise to power of number_of_month
#print out the initial_deposit_amount

number_of_month = int(input('input number of month:'))

final_accout_value = 5000

mothly_interest_rate = 4.25
	
initial_deposit_amount = final_accout_value / (1+mothly_interest_rate)**number_of_month

print(f"the initial amount is: {initial_deposit_amount}")



