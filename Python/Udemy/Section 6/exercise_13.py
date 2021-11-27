# MRO - Method Resolution Order
# Rule that Python follows to determine which method to run

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C ):
    pass

# this MRO is A -> B and C -> D
# check with 
print(D.__mro__)
# helpful for debugging
