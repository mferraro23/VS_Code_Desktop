class PlayerCharacter:
    # class attributes
    new_player = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        # used to instanciate an object inside the class
        return cls('Teddy', num1 + num2)

    @staticmethod
    def add_more(num1, num2):
        # same as classmethod but does not have access to cls, can only call functions and cannot create objects
        return num1 + num2


# can use classmethod to call methods inside of a class without instanciating the class object.
player_2 = PlayerCharacter.adding_things(2, 3)
print(player_2.age)
