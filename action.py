import random

from entity import Herbivore, Grass, Rock, Predator, Tree, Creature


class Actions:
    def __init__(self, simulation_):
        self.entity_dict = simulation_.entity_dict
        self.map = simulation_.map

    def init_actions(self):

        cells_fill = set(list(self.map.map_dict.keys()))
        for entity_, amount in self.entity_dict.items():
            cells = set(random.sample(list(cells_fill), amount))
            for cell in cells:
                match entity_:
                    case 'herb':
                        self.map.add_entity(Herbivore(cell))
                    case 'grass':
                        self.map.add_entity(Grass(cell))
                    case 'rock':
                        self.map.add_entity(Rock(cell))
                    case 'predator':
                        self.map.add_entity(Predator(cell))
                    case 'tree':
                        self.map.add_entity(Tree(cell))
            cells_fill = cells_fill - cells

    def turn_actions(self):
        #self.map.add_entity(Empty(random.choice(list(self.map.map_dict.keys()))))
        creatures = []
        for entity in self.map.map_dict.values():
            if isinstance(entity, Creature):
                creatures.append(entity)
        for creature in creatures:
            creature.make_move(self.map)

