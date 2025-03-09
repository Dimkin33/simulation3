import tkinter as tk
from collections import Counter


class Render:

    def __init__(self, simulation_):

        self.root = tk.Tk()

        self.map = simulation_.map.map_dict
        self.action = simulation_.action
        self.width, self.height = simulation_.width, simulation_.height
        self.root.title(f"simulation {self.width} x {self.height}")
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
                hp = getattr(entity, "hp", "")
                cell = tk.Label(self.frame_grid, text=f"{name[0]}({hp})", borderwidth=1, relief="solid", width=8, height=3, bg = color)
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
