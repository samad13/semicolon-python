passed = int(0)
fail = int(0)
for len in range(15):
	scores = int(input("input the student scores: "))
	if(scores >= 45):
		passed+=1
	elif(scores < 45):
		fail+=1
print("passs: ", passed, "fail: ", fail )