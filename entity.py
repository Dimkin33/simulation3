class Entity:
    def __init__(self):
        self.hp = None  # Лучше None, чем '', если это число
    def make_move(self, coord):
        pass


class Rock(Entity):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родителя
        self.speed = 0
        self.name = 'Rock'
        self.colour = 'gray'

class Grass(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.name = 'Grass'
        self.colour = 'green'
        self.hp = 10

class Tree(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.name = 'Tree'
        self.colour = 'brown'

class Creature(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.name = 'Creature'
        self.hp = 10

    def make_move(self, coord):
        pass
class Herbivore(Creature):
    def __init__(self):
        super().__init__()
        self.speed = 1  # Например, двигается быстрее
        self.name = 'Herb'
        self.colour = 'yellow'
        self.hp = 10

class Predator(Creature):
    def __init__(self):
        super().__init__()
        self.speed = 2  # Например, быстрее, чем Herbivore
        self.name = 'Predator'
        self.colour = 'red'
        self.hp = 10

class Empty(Entity):
    def __init__(self):
        super().__init__()
        self.name = ' '
        self.colour = 'white'

