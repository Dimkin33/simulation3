from entity import Empty


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_dict = {(x, y): Empty() for x in range(self.width) for y in range(self.height)}

    def add_entity(self, entity_, coord):
        self.map_dict[coord] = entity_

    def remove_entity(self, x, y):
        self.map_dict[(x,y)] = Empty()

