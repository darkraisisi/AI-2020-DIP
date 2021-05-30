from typing import List
from computer import Acceptor, Proposer, Learner
from message import Message
from network import Network
from matrix import Matrix

class Simulation():
    def __init__(self, fileName: str) -> None:
        with open(fileName, 'r') as file:
            events = file.readlines()
            events = list(map(lambda x: x.rstrip('\n').split(' ', 3), events))
            nP, nA, nL, tmax = events[0]
            self.events = events[1:]
            self.tmax = int(tmax)
            self.computers = []
            self.network = Network()
            self.matrix = Matrix()

            for i in range(int(nP)):
                self.network.P.append(Proposer(i, self.network))

            for i in range(int(nA)):
                self.network.A.append(Acceptor(i, self.network))

            for i in range(int(nL)):
                self.network.L.append(Learner(i, self.network, self.matrix.addLetters))
            
            if int(nL) > 0:
                self.endFunc = self.matrix.saveAll
            else:
                self.endFunc = None

    def simulation(self):
        """
        nP (int): amount of Proposers
        nA (int): amount of Acceptors
        tmax (int): Length of the sim in ticks.
        E (list): Orderd list with events [e1, e2 ...], orderd by tick number.
            t (int): tick where this takes place 0>t<tmax
            msgType: (list): A name given to the type of message.
            msgR (Computer): Who is supposed to recieve this message.
            msgV (x): Suggested value to propagate. 
        """
        
        for tick in range(self.tmax):
            self.network.currentTick = tick
            if len(self.network.queue) == 0 and len(self.events) == 1:
                # If there are no messages or events the simulation is done.
                if self.endFunc != None:
                    self.endFunc()
                break
            
            # Verwerk event e (als dat tenminste bestaat)
            if int(self.events[0][0]) == tick:
                e = self.events[0]
                (t, msgType, msgR, msgV) = e
                del self.events[0]

                if msgType == 'FAIL':
                    if msgR == 'ACCEPTOR':
                        self.network.A[int(msgV)-1].failed = True
                        self.network.printMsg(tick, f'** A{int(msgV)} kapot **')

                    elif msgR == 'PROPOSER':
                        self.network.P[int(msgV)-1].failed = True
                        self.network.printMsg(tick, f'** P{int(msgV)} kapot **')

                if msgType == 'RECOVER':
                    if msgR == 'ACCEPTOR':
                        self.network.A[int(msgV)-1].failed = False
                        self.network.printMsg(tick, f'** A{int(msgV)} gerepareerd  **')

                    elif msgR == 'PROPOSER':
                        self.network.P[int(msgV)-1].failed = False
                        self.network.printMsg(tick, f'** P{int(msgV)} gerepareerd  **')

                if msgType == 'PROPOSE':
                    m = Message(None, self.network.P[int(msgR)-1], 'PROPOSE', msgV)
                    m.dst.recieveMessage(m)
                else:
                   self.getMessage()
            
            else:
                self.getMessage()

        print('')
        for proposer in self.network.P:
            if proposer.value is not None:
                print(
                    f'P{proposer.id} heeft wel consensus (voorgesteld: {proposer.proposedValue}, geaccepteerd: {proposer.value})')
            else:
                print(f'P{proposer.id} heeft geen consensus')


    def getMessage(self):
        m = self.network.extractMessage()
        if (m is not None):
            m.dst.recieveMessage(m)
        else:
            self.network.printMsg(self.network.currentTick, '')