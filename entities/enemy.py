from entities import entity


class Enemy(entity.Entity):
    def __init__(self):
        super().__init__()
        self.heal_rate = 0


class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Zombie"
        self.health = 45
        self.base_damage = 10


class DemonEye(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Demon Eye"
        self.health = 60
        self.base_damage = 18


class Harpy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Harpy"
        self.health = 100
        self.base_damage = 25