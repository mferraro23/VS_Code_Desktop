# Decorators
# @classmethod
# @staticmethod
# they supercharge our function, it adds extra functionality to it

# Must understand higher order function (HOF)
# a higher order function is a function that either accepts a func as a param or returns a funcation

# HOF
# takes function
def my_decorator(func):
    # takes arguments/parameters
    def wrap_func(*args, **kwargs): # decorator pattern
        print('******')
        func(*args, **kwargs)
        print('******')
    return wrap_func

# hello gets automatically wrapped by decorator
@my_decorator
def hello(greeting):
    print(greeting)


# wraps the function in another function where you can pass a function through
# same as
# a = my_decorator(hello)
# print(a)

message = 'hiii'
hello(message)
