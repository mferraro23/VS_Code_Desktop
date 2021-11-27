class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age, sounds):
        self.name = name
        self.age = age
        self.sounds = sounds

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Nox(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Nox('Nox', 2, 'Meows'), Simon('Simon',4, 'Purs'), Sally("Sally", 5, 'Growls')]

my_pets = Pets(my_cats)

my_pets.walk()

#4 Output all of the cats walking using the my_pets instance
