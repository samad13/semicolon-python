#collect the subtotal and save it in variable
#collect the gratiuty and save it in variable
#multiply 0.01 by gratiuty to get gratiuty_percentage;
#multiply gratiuty_percentage by subtotal to get the gratiuty amount
#add gratiuty_amaount with subtotal to get total
#print out gratiuty_amount and total



subtotal = int(input('put in subtotal:'))

gratiuty = int(input('put in gratiuty:'))


gratiuty_percentage =gratiuty * 0.01

gratiuty_amount = gratiuty_percentage * subtotal

total = gratiuty_amount + subtotal

print(f"gratiuty: {gratiuty_amount} and total:  {total}")
