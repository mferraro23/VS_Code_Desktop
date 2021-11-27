# OOP

class PlayerCharacter:
    # Class object attribute
    membership = True  # it will be true and exist for all objects, you cannot change it

    # self needs to be used as a param of any def in class objects
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            # attributes
            self.name = name
            self.age = age

    def run(self):
        return 'run'


player1 = PlayerCharacter('Mike', 20)
print(player1.name)
print(player1.run())
