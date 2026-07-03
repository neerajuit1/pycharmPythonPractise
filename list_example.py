numbers = ['zero', 'one', 'two', 'three', 'four', 'five']
print(numbers)
numbers_len_four = []

for number in numbers:
     if len(number) == 4:
         numbers_len_four.append(number)

print (numbers_len_four)

values = [1,2,3,4,5,6,7,8,9,10]
value_odd = [value for value in values if value%2==1]
value_even = [value for value in values if value%2==0]

print (f'orignial values {values}')
print (f'odd values {value_odd}')
print (f'even values {value_even}')