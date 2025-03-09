import tkinter as tk
import random
from collections import Counter

from entity.entity import Herbivore, Predator, Grass, Rock, Tree, Empty


class Render:

    def __init__(self, simulation_):

        self.root = tk.Tk()
        self.root.title("simulation")
        self.map = simulation_.map.map_dict
        self.action = simulation_.action
        self.width, self.height = simulation_.width, simulation_.height

        self.button_next = tk.Button(self.root, text="Обновить", command = self.on_button_click)
        self.button_next.pack(side="right", padx=10, pady=10)

        self.frame_grid = tk.Frame(self.root)
        self.frame_grid.pack(side = 'left')

        self.display_grid()
        self.update_label()

    def display_grid(self):
       # Отображение сетки

        for i in range(self.width):
            for j in range(self.height):
                entity = self.map[(i, j)]
                color = getattr(entity, "colour", "white")  # Получаем цвет или белый
                name = getattr(entity, "name", "")  # Получаем имя или "Empty"
                cell = tk.Label(self.frame_grid, text=f"{name}", borderwidth=1, relief="solid", width=8, height=3, bg = color)
                cell.grid(row=i, column=j, padx=2, pady=2)

    def update_label(self):
        """Обновляет текстовое поле справа"""
        value_counts = Counter(v.name for v in self.map.values())
        text = '\n'.join(f"{key}: \t {value}" for key, value in value_counts.items())

        if hasattr(self, "label"):  # Если метка уже создана, обновляем
            self.label.config(text=text)
        else:  # Создаем метку в первый раз
            self.label = tk.Label(self.root, text=text, font=("Arial", 14), justify="left")
            self.label.pack(pady=20, side='right', anchor="n")


    def on_button_click(self):
        """Событие нажатия кнопки"""
        print("Кнопка нажата!")  # Вывод в консоль
        self.action.turn_actions()
        self.display_grid()  # Обновляем сетку
        self.update_label()



    def render(self):
        self.root.mainloop()


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_dict = {(x, y): Empty() for x in range(self.width) for y in range(self.height)}

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


# Запуск симуляции
if __name__ == '__main__':
    entity_dict = {'herb': 12, 'grass': 15, 'rock': 10, 'tree': 10, 'predator': 12}
    simulation = Simulation(15, 10, entity_dict)
    simulation.run()
