import random
from entity import Herbivore, Grass, Rock, Predator, Tree, Empty


class Actions:
    def __init__(self, simulation_):
        self.entity_dict = simulation_.entity_dict
        self.map = simulation_.map


    def init_actions(self):
        self.map.map_dict = {(x, y): Empty((x, y)) for x in range(self.map.width) for y in range(self.map.height)}
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
        herbivores, predators = [], []
        for entity in self.map.map_dict.values():
            if isinstance(entity, Herbivore):
                herbivores.append(entity)
            elif isinstance(entity, Predator):
                predators.append(entity)

        for herbivore in herbivores:
            herbivore.make_move(self.map)
            herbivore.hungred(self.map)
        for predator in predators:
            predator.make_move(self.map)
            predator.make_move(self.map)
            predator.hungred(self.map)

