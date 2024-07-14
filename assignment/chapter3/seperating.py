five = input('put five integer: ')
if len(five) != 5:
    print(" please enter exactly a five-digit.")
else:
    for num in five:
        print(num, end=" ")
