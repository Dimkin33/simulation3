from action import Actions
from map import Map
from render import Render


class Simulation:
    def __init__(self, width, height, entity_):
        self.width, self.height = width, height
        self.entity_dict = entity_
        self.map = Map(width, height)

        self.action = Actions(self)
        self.action.init_actions()
        self.render = Render(self)




    def run(self):
        #pass
        self.render.render()
