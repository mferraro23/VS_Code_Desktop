class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return("logged in!")


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # or use super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Wizard is attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        User.__init__(self, email)  # or use super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(
            f"Archer is attacking with arrows: arrows left: {self.num_arrows}")


def player_attack(charcter):
    charcter.attack()


wizard_1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer_1 = Archer("Robin", 100)

print(wizard_1.email)
# player_attack(wizard_1)
# player_attack(archer_1)
