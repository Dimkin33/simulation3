from simulation import Simulation

# Запуск симуляции
if __name__ == '__main__':
    entity_dict = {'herb': 3, 'grass': 2, 'rock': 10, 'tree': 10, 'predator': 1}
    simulation = Simulation(10, 10, entity_dict)
    simulation.run()
