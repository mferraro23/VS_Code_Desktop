# filter practice
# decides whether it should be filtered or not
# if true add to new list if it is false it doesnt add it

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_if_odd(item):
    return item % 2 != 0


list_of_odd = list(filter(check_if_odd, my_list))
print(list_of_odd)
