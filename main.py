from Simulation import Simulation

# Запуск симуляции
if __name__ == '__main__':
    entity_dict = {'herb': 12, 'grass': 15, 'rock': 10, 'tree': 10, 'predator': 12}
    simulation = Simulation(15, 10, entity_dict)
    simulation.run()
