# Decorator Practice

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f'it took {time_2-time_1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()
