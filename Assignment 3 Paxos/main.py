from simulation import Simulation

if __name__ == '__main__':
    # Runs all the simulation examples.
    # files = ['input/input1.txt', 'input/input2.txt']
    files = ['input/input2.txt']


    for file in files:
        # try:
        #     sim = Simulation(file)
        #     sim.simulation()
        # except Exception as e:
        #     print(e)
        
        sim = Simulation(file)
        sim.simulation()