class Animal:
    alive = []

    def __init__(self, name: str, health: str = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def animal_alive(self) -> bool:
        return self.health > 0

    def animal_dead(self) -> bool:
        if self.health <= 0:
            Animal.alive.remove(self)
            return True
        return False

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def print_alive(cls) -> str:
        return "[" + ", ".join(str(animal) for animal in cls.alive) + "]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.animal_dead()
