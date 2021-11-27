# dictionary comprehension

# key and value pair, value gets acted upon
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)

my_dict = {k:k*2 for k in [1,2,3] }
print(my_dict)