#divide minutes by 525600 which is minutes per year
#modulo minutes by 525600 which is minutes per year to  get remaider
#divide remaider 1440 perday
#print out the result

minutes = int(input('put in minutes:'))

per_year = minutes //  525600

remainder = minutes %  525600
	
per_day = remainder //  1440

print(f"{per_year} year and {per_day} days")



