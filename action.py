import random

from entity.entity import Herbivore, Grass, Rock, Predator, Tree, Empty


class Actions:
    def __init__(self, simulation_):
        self.entity_dict = simulation_.entity_dict
        self.map = simulation_.map.map_dict

    def init_actions(self):

        cells_fill = set(list(self.map.keys()))
        for entity_, amount in self.entity_dict.items():
            cells = set(random.sample(list(cells_fill), amount))
            for cell in cells:
                match entity_:
                    case 'herb':
                        self.map[cell] = Herbivore()
                    case 'grass':
                        self.map[cell] = Grass()
                    case 'rock':
                        self.map[cell] = Rock()
                    case 'predator':
                        self.map[cell] = Predator()
                    case 'tree':
                        self.map[cell] = Tree()
            cells_fill = cells_fill - cells

    def turn_actions(self):
        self.map[random.choice(list(self.map.keys()))] = Empty()
