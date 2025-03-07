import tkinter as tk
import entity
import random
class Render:

    def __init__(self, map_dict):
        self.width, self.height = (list(map_dict.items())[-1][0])
        print(self.width, self.height)
        self.root = tk.Tk()
        self.root.title("simulation")
        #self.root.geometry("300x250")

        for i in range(10):
            for j in range(10):
                cell = tk.Label(self.root, text=f"{map_dict[(i, j)]}", borderwidth=1, relief="solid", width=6, height=2)
                cell.grid(row=i, column=j, padx=2, pady=2)

    def render(self):
        self.root.mainloop()


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_dict = {(x, y): (x,y) for x in range(self.width) for y in range(self.height)}

class Simulation:
    def __init__(self, width, height):
        self.map_simulation = Map(width, height)
        Actions().init_actions()
        Render(self.map_simulation.map_dict).render()

    def run(self):
        pass



class Actions:
    def __init__(self):
        self.entity_dict = {'herbivore': 12, 'grass': 15, 'rock': 10, 'tree': 10, 'predator': 12}
    def init_actions(self):
        for entity_, amount in self.entity_dict.items():

            print(entity_, amount)


    def turn_actions(self):
        pass

# Запуск симуляции

simulation = Simulation(10, 10)
simulation.run()
