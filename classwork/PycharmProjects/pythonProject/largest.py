"""""def biggest_odd(numbers):
    largest_odd = 0
    for letters in numbers:
        number = int(letters)
        if number % 2 != 0:
             if number > largest_odd:
                largest_odd = number
    return  largest_odd
print(biggest_odd("23956"))


def equal_string(a, b):
    count = 0
    if(len(a) == len(b)):
        print(a)
        for i in a:
            cha = list(b)
            for i in cha:
                count +=1
            print(count)
               # print( print(i))
            if count == len(cha):
                print(i)
                return True
    else:
        return False

print(equal_string("lol", b"lol"))"""""



def createDick(ls):
    dick = {}
    for num in ls:
        val = num**3
        dick[num] = val
    return dick
print(createDick([1,2,3,4,5]))
