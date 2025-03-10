from entity import Empty

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_dict = {(x, y): Empty((x, y)) for x in range(self.width) for y in range(self.height)}

    def add_entity(self, entity_):
        self.map_dict[entity_.cell] = entity_


    def get_entity(self, cell):
        return self.map_dict[cell]