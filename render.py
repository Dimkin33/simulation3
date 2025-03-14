import tkinter as tk
import copy
from collections import Counter
from time import sleep

from entity import Empty


class Render:
    def __init__(self, simulation_):
        self.root = tk.Tk()
        self.simulation = simulation_
        self.map = simulation_.map
        self.action = simulation_.action
        self.width, self.height = simulation_.width, simulation_.height
        self.history = simulation_.history
        self.root.title(f"Simulation {self.width} x {self.height}")
        self.paused = False
        self.auto_running = False  # Добавляем атрибут
        # Кадр для кнопок
        self.frame_button = tk.Frame(self.root)
        self.frame_button.pack(side="bottom", pady=10)

        # Кнопки управления
        self.button_prev = tk.Button(self.frame_button, text="Previous", command=self.on_button_prev_click)
        self.button_next = tk.Button(self.frame_button, text="Next", command=self.on_button_next_click)
        self.button_exit = tk.Button(self.frame_button, text="Exit", command=self.root.destroy)
        self.button_restart = tk.Button(self.frame_button, text="Restart", command=self.restart_simulation)
        self.button_auto = tk.Button(self.frame_button, text="Auto", command=self.on_button_auto_click)

        self.button_auto = tk.Button(self.frame_button, text="Auto", command=self.toggle_auto_pause)

        self.button_auto.pack(side="right", padx=10)
        self.button_prev.pack(side="left", padx=10)
        self.button_next.pack(side="left", padx=10)
        self.button_auto.pack(side="left", padx=10)

        self.button_restart.pack(side="left", padx=10)
        self.button_exit.pack(side = 'left', padx=10)

        # Кадр для сетки
        self.frame_grid = tk.Frame(self.root)
        self.frame_grid.pack(side="left")

        self.display_grid()
        self.update_label()



    def restart_simulation(self):
        self.paused = False
        self.simulation.count_simulation = 0
        self.simulation.history.clear()
        self.action.init_actions()  # Пересоздаём сущности
        self.display_grid()  # Обновляем интерфейс
        self.simulation.run()

    def toggle_auto_pause(self):
        self.auto_running = not self.auto_running
        self.button_auto.config(text="Pause" if self.auto_running else "Auto")

        while self.auto_running and self.map.count_all_health():
            self.on_button_next_click()
            self.root.update()

    def display_grid(self):
        """Отображение сетки"""
        for widget in self.frame_grid.winfo_children():
            widget.destroy()  # Удаляем старые виджеты перед обновлением

        for i in range(self.width):
            for j in range(self.height):
                entity = self.map.map_dict[(i, j)]
                color = getattr(entity, "colour", "white")  # Получаем цвет или белый
                name = getattr(entity, "name", "?")  # Получаем имя или "?"
                hp = getattr(entity, "hp", "")

                cell = tk.Label(
                    self.frame_grid, text=f"{name[0] if name[0] != 'E' else ''} {hp if hp else ''}",
                    borderwidth=1, relief="solid",
                    width=8, height=3, bg=color
                )
                cell.grid(row=i, column=j, padx=2, pady=2)

        self.update_label()

    def update_label(self):
        """Обновляет текстовое поле справа"""
        value_counts = Counter(v.name for v in self.map.map_dict.values())
        text = '\n'.join(f"{key}: {value}" for key, value in value_counts.items())

        if hasattr(self, "label"):  # Если метка уже создана, обновляем
            self.label.config(text=text)
        else:  # Создаем метку в первый раз
            self.label = tk.Label(self.root, text=text, font=("Arial", 14), justify="left")
            self.label.pack(pady=20, side='right', anchor="n")

    def on_button_prev_click(self):
        """Откат к предыдущему шагу"""
        #print('button prev')
        self.simulation.count_simulation -= 1
        if  self.simulation.count_simulation > 0:
            print(f' Simation_ step {self.simulation.count_simulation}')
        if self.history:
            previous_map = self.history.pop()  # Получаем предыдущее состояние
            self.map.map_dict = copy.deepcopy(previous_map.map_dict)  # Обновляем содержимое карты
            for cell, entity in self.map.map_dict.items():
                entity.cell = cell  # Обновляем координаты сущностей
            self.display_grid()

        else:
            print("Нет предыдущих состояний!")

    def on_button_next_click(self):
        """Переход к следующему шагу"""
        #print('Button next')
        self.simulation.count_simulation += 1
        print(f' Simation_ step {self.simulation.count_simulation}')
        self.history.append(copy.deepcopy(self.map))  # Сохраняем копию карты
        self.action.turn_actions()
        #self.root.update()
        self.display_grid()

    def on_button_auto_click(self):
        while self.map.count_all_health():
            if self.paused:
                self.root.update()
                continue  # Ждем, пока пользователь не снимет паузу

            self.on_button_next_click()
            self.root.update()
        print('Все померли')

    def render(self):
        self.root.mainloop()
