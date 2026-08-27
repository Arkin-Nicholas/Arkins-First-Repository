#RPG Hero Game
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage!")

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)
print(f"{arthur.name}'s remaining HP: {arthur.hp}")
print(f"{morgana.name}'s remaining HP: {morgana.hp}")
