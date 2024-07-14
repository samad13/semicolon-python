money = int(input('input your initial investment: '))
investment=0
annual_interest = 0.07
for len in range(1,30 +1):
	investment +=  money * (1 + annual_interest) ** len
	print(f"At the end of year {len}, you will have ${investment:.2f}")
print(f"${investment:.2f}")
