# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Londan", 15)
cat2 = Cat("Nox", 2)
cat3 = Cat("Georgie", 19)
# 2 Create a function that finds the oldest cat


def find_oldest_cat(*args):
    max_age = 0
    for i in args:
        if i > max_age:
            max_age = i
    return max_age


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {find_oldest_cat(cat1.age,cat2.age,cat3.age)}")
