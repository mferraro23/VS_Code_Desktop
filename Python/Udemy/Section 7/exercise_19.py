# lambda expressions
# anon function

# lambda parameter: action, data


my_list = [1, 2, 3]
my_list_2 = [10, 20, 30]

# old way


def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, my_list)))

# new way

print(list(map(lambda item: item*2, my_list)))


print(list(filter(lambda item: item % 2 != 0, my_list)))

