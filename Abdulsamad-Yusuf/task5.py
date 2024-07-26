#collect the number and save it in variable
#get the remainder from the number with 10 using modulo operator and save it in value1
#floor divide the number  with 100 and save it in value2;
#floor divide the number  with 10 and save it in value3;
#get the remainder from the value3 with 10 using modulo operator and save it in value4
#add value1 value2 and value4 together to get the answer



number = int(input('put in integer:'))

value1 = number % 10
value2 = number // 100
value3 = number // 10
value4 = value3 % 10



print(value1 + value2 + value4)
