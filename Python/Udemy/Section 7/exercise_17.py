# reduce learning
from functools import reduce

# reduce needs function, sequnce or data 

my_list = list(range(51))

def accumulator(acc, item):
    print(f'{acc}, {item}')
    return acc + item

print(reduce(accumulator, my_list, 1))
