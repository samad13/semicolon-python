money = int(input('input your initial investment: '))
investment=0
annual_interest = 0.07
for len in range(30):
	investment +=  money * annual_interest
print(investment)