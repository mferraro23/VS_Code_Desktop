#check duplicates
some_list =['a','b','c','b','d','m','n','n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        duplicates.append(value)

new_set = set(duplicates)
print(new_set)