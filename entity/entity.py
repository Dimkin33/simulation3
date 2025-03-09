class Entity:
    def __init__(self):
        self.hp = 100
    # def __str__(self):
    #     return f'{self.__class__.__name__}'

class Rock(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Rock'
        self.colour = 'gray'
class Grass(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Grass'
        self.colour = 'green'
class Tree(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Tree'
        self.colour = 'brown'
class Creature(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Creature'
class Herbivore(Creature):
    def __init__(self):
        self.speed = 0
        self.name = 'Herb'
        self.colour = 'yellow'
class Predator(Creature):
    def __init__(self):
        self.speed = 0
        self.name = 'Predator'
        self.colour = 'red'
class Empty(Entity):
    def __init__(self):
        self.name = ''
        self.colour = 'white'
