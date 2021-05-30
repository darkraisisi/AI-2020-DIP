from simulation import Simulation

if __name__ == '__main__':
    # Runs all the simulation examples.
    files = ['input/input1.txt', 'input/input2.txt','input/input3.txt']


    for file in files:
        sim = Simulation(file)
        sim.simulation()