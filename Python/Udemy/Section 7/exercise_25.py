# comprehension exercise

my_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = list({char for char in my_list if my_list.count(char)>1})
print(duplicates)
