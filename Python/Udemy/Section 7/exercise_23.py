# set comprehensions
# set is same as list

# syntax
# my_set = [param for param in iterable (optional: conditional)]


my_set = {}


# for each element in iterable add to this list
my_set = {char for char in 'hello'}
print(my_set)

my_set = {num for num in range(0, 100)}
print(my_set)

my_set = {num**2 for num in range(0, 100)}
print(my_set)

my_set_2 = {num for num in my_set if num % 2 == 0}
print(my_set_2)
