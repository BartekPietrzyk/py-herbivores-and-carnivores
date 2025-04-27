class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    def animal_alive(self) -> bool:
        return self.health > 0

    def animal_dead(self) -> bool:
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)
            return True
        return False

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.animal_dead()

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
            herbivore.take_damage(50)
