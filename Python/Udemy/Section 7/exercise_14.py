# map learning

# map(function, iterable)
# action, daTa we want to take action on

# new way
my_list = [1,2,3]
def multiply_by_2(item):
    return item * 2


mapped_func = list(map(multiply_by_2, my_list))
print(mapped_func)

# old way
'''
def multiply_by_2(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return new_list
print(multiply_by_2([1,2,3]))
'''
