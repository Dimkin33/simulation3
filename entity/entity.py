class Entity:
    def __init__(self):
        self.hp = ''
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
        self.hp = 10
class Tree(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Tree'
        self.colour = 'brown'
class Creature(Entity):
    def __init__(self):
        self.speed = 0
        self.name = 'Creature'
        self.hp = 10
class Herbivore(Creature):
    def __init__(self):
        self.speed = 0
        self.name = 'Herb'
        self.colour = 'yellow'
        self.hp = 10
class Predator(Creature):
    def __init__(self):
        self.speed = 0
        self.name = 'Predator'
        self.colour = 'red'
        self.hp = 10
class Empty(Entity):
    def __init__(self):
        self.name = ' '
        self.colour = 'white'
