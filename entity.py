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
        """Поиск ближайшей цели с помощью BFS"""
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(self.cell, [])])  # (координаты, путь)
        visited = set()

        while queue:
            cell, path = queue.popleft()

            if cell in visited:
                continue
            visited.add(cell)

            # Если нашли цель, возвращаем путь
            if isinstance(game_map.map_dict[cell], target_class):
                return path

                # Добавляем в очередь соседние клетки
            for dx, dy in directions:
                new_cell = (cell[0] + dx, cell[1] + dy)
                if new_cell in game_map.map_dict and isinstance(game_map.map_dict[new_cell], (Empty, target_class)):
                    queue.append((new_cell, path + [new_cell]))

        return None  # Цель не найдена

    def move_to(self, game_map, path):
        """Перемещение по найденному пути"""
        if path:

            game_map.add_entity(Empty(self.cell))  # Очищаем старую клетку
            self.cell = path[0]  # Двигаемся на первую клетку пути
            game_map.add_entity(self)  # Добавляем себя на новую позицию

    def make_move(self, game_map):
        """Ищем цель и двигаемся к ней"""
        target_map = {Herbivore: Grass, Predator: Herbivore}
        target_class = target_map.get(type(self))  # Получаем целевой класс
        if target_class:
            path = self.bfs(game_map, target_class)
            if path:  # Проверяем, найден ли путь
                self.move_to(game_map, path)


class Herbivore(Creature):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 1  # Медленнее хищника
        self.name = 'Herb'
        self.colour = 'yellow'
        self.hp = 10  # Начальное здоровье

    def make_move(self, game_map):
        """Ест траву, если она рядом, иначе двигается к ней"""
        # Проверяем, есть ли трава рядом
        neighbors = [(self.cell[0] + dx, self.cell[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for neighbor in neighbors:
            if isinstance(game_map.map_dict.get(neighbor), Grass):
                self.eat_grass(game_map, neighbor)
                return  # Если поели, ход завершается

        # Если травы рядом нет, двигаемся к ближайшей
        path = self.bfs(game_map, Grass)
        if path:
            self.move_to(game_map, path)

    def eat_grass(self, game_map, target_cell):
        """Травоядное съедает траву и восстанавливает здоровье"""
        grass = game_map.map_dict[target_cell]
        if isinstance(grass, Grass):
            print(f"{self.name} съедает {grass.name} и восстанавливает {grass.hp} HP!")
            self.hp += grass.hp  # Восстанавливаем здоровье
            game_map.add_entity(Empty(target_cell))  # Убираем траву с карты



class Predator(Creature):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 2  # Хищник быстрее травоядного
        self.name = 'Predator'
        self.colour = 'red'
        self.hp = 10
        self.attack_power = 2  # Сила атаки

    def make_move(self, game_map):
        """Атакует травоядное или двигается к нему"""
        # Проверяем, есть ли рядом жертва
        neighbors = [(self.cell[0] + dx, self.cell[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for neighbor in neighbors:
            if isinstance(game_map.map_dict.get(neighbor), Herbivore):
                self.attack(game_map, neighbor)
                return  # Если атаковали, ход завершается

        # Если жертвы рядом нет, двигаемся к ближайшей
        path = self.bfs(game_map, Herbivore)
        if path:
            self.move_to(game_map, path)

    def attack(self, game_map, target_cell):
        """Атакует травоядное"""
        target = game_map.map_dict[target_cell]
        if isinstance(target, Herbivore):
            print(f"{self.name} атакует {target.name} на {self.attack_power} урона!")
            target.hp -= self.attack_power
            if target.hp <= 0:
                print(f"{target.name} погибает!")
                game_map.add_entity(Empty(target_cell))  # Убираем жертву с карты




