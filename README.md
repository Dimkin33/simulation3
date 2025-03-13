# Simulation Project

## Описание

Этот проект представляет собой симуляцию экосистемы с травоядными, хищниками, травой, камнями и деревьями. Используется графический интерфейс на `Tkinter`, а также реализована логика движения и взаимодействия сущностей.

## Функциональность

- Генерация случайной карты с объектами
- Движение травоядных к траве, а хищников к травоядным
- Голодание и смерть существ
- Отрисовка симуляции в окне с кнопками управления
- Возможность приостановки и возобновления симуляции

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/Dimkin33/simulation-project.git
cd simulation-project
```

### 2. Установка зависимостей

Убедитесь, что у вас установлен Python 3. Затем установите необходимые библиотеки:

```bash
pip install -r requirements.txt
```

(Файл `requirements.txt` нужно создать, если он отсутствует, добавив туда `tkinter` и другие зависимости.)

### 3. Запуск симуляции

```bash
python main.py
```

## Управление

- **Next** — следующий шаг симуляции
- **Previous** — возврат к предыдущему шагу
- **Auto** — автоматический режим до завершения симуляции
- **Pause** — пауза/возобновление
- **Restart** — перезапуск симуляции
- **Exit** — выход

## Структура проекта

```
📂 simulation-project
├── action.py      # Логика действий существ
├── entity.py      # Определение классов существ
├── map.py         # Карта с сущностями
├── render.py      # Графический интерфейс
├── simulation.py  # Главный класс симуляции
├── main.py        # Точка входа в программу
├── requirements.txt # Зависимости проекта
└── README.md      # Описание проекта
```

## Лицензия

Этот проект распространяется под лицензией MIT. Свободно используйте и модифицируйте его!

