from collections import deque


class Entity:
    def __init__(self, cell):
        self.cell = cell
        self.hp = None  # Лучше None, чем '', если это число

    def make_move(self, game_map):
        pass

class Empty(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.name = 'Empty'
        self.colour = 'white'

class Rock(Entity):
    def __init__(self, cell):
        super().__init__(cell)  # Вызываем конструктор родителя
        self.speed = 0
        self.name = 'Rock'
        self.colour = 'gray'


class Grass(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 0
        self.name = 'Grass'
        self.colour = 'green'
        self.hp = 10


class Tree(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 0
        self.name = 'Tree'
        self.colour = 'brown'


class Creature(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 0
        self.name = 'Creature'
        self.hp = 10

    def bfs(self, game_map, target_class):
        """Поиск ближайшей цели (например, травы) с помощью BFS"""
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(self.cell, [])])  # (координаты, путь)
        visited = set()

        while queue:
            cell, path = queue.popleft()
            #print(cell, game_map.map_dict[cell].name, path)
            if cell in visited:
                continue
            visited.add(cell)

            # Проверяем, является ли эта клетка целью

            if isinstance(game_map.map_dict[cell], target_class):
                return path  # Возвращаем путь до цели

            # Добавляем соседей в очередь
            for dx, dy in directions:
                new_cell = (cell[0] + dx, cell[1] + dy)
                if new_cell in game_map.map_dict and isinstance(game_map.map_dict[new_cell], (Empty, target_class)):
                    queue.append((new_cell, path + [new_cell]))

        return None  # Если путь не найден

    def move_to(self, game_map, path):
        """Двигаемся по найденному пути"""
        if path:
            game_map.add_entity(Empty(self.cell))  # Очищаем старую клетку
            self.cell = path[0]  # Берем первый шаг из пути
            game_map.add_entity(self)  # Перемещаем объект


    def make_move(self, game_map):
        """Ищем цель и двигаемся к ней"""
        path = None
        if isinstance(self, Herbivore):
            path = self.bfs(game_map, Grass)
        if isinstance(self, Predator):
            path = self.bfs(game_map, Herbivore)
        self.move_to(game_map, path)


class Herbivore(Creature):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 1  # Например, двигается быстрее
        self.name = 'Herb'
        self.colour = 'yellow'
        self.hp = 10


class Predator(Creature):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 2  # Например, быстрее, чем Herbivore
        self.name = 'Predator'
        self.colour = 'red'
        self.hp = 10



