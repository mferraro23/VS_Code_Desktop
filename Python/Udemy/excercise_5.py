def highest_even(li):
    max_value = 0
    for args in li:
        if args % 2 == 0:
            if args > max_value:
                max_value = args
    return max_value

print(highest_even([1,2,3,6,10,11]))