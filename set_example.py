set_first = {1,2,3,3}
set_second = {4,5,6,7}
print(f'beforeadding{set_first}')
set_first.add(5)
print(f'after adding{set_first}')

list_first = [1,2,3,4,5,6,7,8,8,10]

list_to_set = set (list_first)
print(f'listfirstconverttoset{list_to_set}')

print(10 in list_to_set)
print ( sum(list_to_set))
set_to_list = list (set_first)
print(set_to_list)