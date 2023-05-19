###For Loop###

number_list=[0,1,2,3,4,5,6,7,8,9]
total_sum_for_loop = 0

for number in number_list:
    print(number)
    total_sum_for_loop += number
    
print(total_sum_for_loop)

###While Loop###

total_sum_while_loop = 0
number_list_length=(len(number_list))
print(number_list_length)
starting_value=0

while starting_value < number_list_length:
    total_sum_while_loop = number_list[starting_value] + total_sum_while_loop
    starting_value += 1

print(total_sum_while_loop)



i = 3

print('This is an example of while loops')

while i < 100000:
   print(i)
   i = i ** 2

