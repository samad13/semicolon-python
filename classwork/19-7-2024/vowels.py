vowels = ""
consonat = ""
words =input("enter a word: ")
for character in words: 
	if character in ["a","e","i","o","u"]:
		vowels += character
	else:
		consonat+=character
print(f" we have {len(set(vowels))} vowels, and {len(set(consonat))}  consonat" )

