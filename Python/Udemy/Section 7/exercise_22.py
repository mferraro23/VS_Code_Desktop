# list comprehensions
# syntax
# my_list = [param for param in iterable (optional: conditional)]


my_list = []

# old way

for char in 'hello':
    my_list.append(char)

print(my_list)

# new way
# for each element in iterable add to this list
my_list = [char for char in 'hello']
print(my_list)

my_list = [num for num in range(0, 100)]
print(my_list)

my_list = [num**2 for num in range(0, 100)]
print(my_list)

my_list_2 = [num for num in my_list if num % 2 == 0]
print(my_list_2)
