import types
from math import ceil
from message import Message
class Computer():
    def __init__(self, _id, network):
        self.id = _id
        self.failed = False
        self.network = network
        self.prior = None
        self.promisedId = 0
    

    def recieveMessage(self, m: Message):
        # Computer komt in actie en voert bericht uit.
        self.network.printMsg(self.network.currentTick, m)


class Proposer(Computer):
    def __init__(self, _id, network):
        super().__init__(_id, network)
        self.amountAccepted = 0
        self.amountRejected = 0
        self.proposedValue = None
        self.value = None
        self.state = None

    def recieveMessage(self, m: Message):
        # Computer komt in actie en voert bericht uit.
        if m.type == 'PROPOSE':
            self.network.printMsg(self.network.currentTick, m)
            self.prior = m.value
            self.proposedValue = m.value
            self.propose(m)
        elif m.type == 'PROMISE':
            self.network.printMsg(self.network.currentTick, m)
            self.promise(m)
        elif m.type == 'ACCEPTED':
            self.accepted(m)
        elif m.type == 'REJECTED':
            self.rejected(m)
        

    def propose(self, m:Message):
        self.network.proposals += 1
        self.promisedId = self.network.proposals
        for acc in self.network.A:
            newM = Message(self, acc, 'PREPARE', None, self.promisedId)
            self.network.queueMessage(newM)
    

    def promise(self, m:Message):
        if self.state != 'promise':
            self.state = 'promise'
            self.amountAccepted = 0
            
        if m.id == self.promisedId:
            self.amountAccepted += 1
            if m.value:
                self.prior = m.value
            if self.amountAccepted > len(self.network.A) // 2:
                for acc in self.network.A:
                    newM = Message(self, acc, 'ACCEPT', self.prior, self.promisedId)
                    self.network.queueMessage(newM)
                self.amountAccepted = 0


    def accepted(self, m:Message):
        if self.state != 'accepted':
            self.state = 'accepted'
            self.amountAccepted = 0

        self.network.printMsg(self.network.currentTick, str(m))
        # print(f'{m.id}, {self.promisedId}')
        if m.id == self.promisedId:
            self.amountAccepted += 1
            if self.amountAccepted > len(self.network.A) // 2:
                self.amountAccepted = 0
                self.consensus(m)

    
    def rejected(self, m:Message):
        self.network.printMsg(self.network.currentTick, str(m))
        if m.id == self.promisedId:
            self.amountRejected += 1
            if self.amountRejected > len(self.network.A) // 2:
                self.amountRejected = 0
                self.propose(m)


    def consensus(self, m):
        self.amountAccepted = 0
        self.amountRejected = 0
        self.value = self.prior
        for learner in self.network.L:
            newM = Message(self, learner, 'SUCCES', self.value, self.promisedId)
            self.network.queueMessage(newM)
                

    
    def __str__(self):
        return f'P{self.id+1}'


class Acceptor(Computer):
    def __init__(self, _id, network):
        super().__init__(_id, network)

    def recieveMessage(self, m: Message):
        if m.type == 'ACCEPT':
            self.accept(m)
        elif m.type == 'PREPARE':
            self.prepare(m)
        elif m.type == 'RESET':
            self.reset(m)

    
    def accept(self, m):
        self.network.printMsg(self.network.currentTick, str(m))
        if self.promisedId <= m.id:
            self.prior = m.value
            newM = Message(self, m.src, 'ACCEPTED', m.value, m.id)
        else:
            newM = Message(self, m.src, 'REJECTED', m.value, m.id)

        self.network.queueMessage(newM)



    def prepare(self, m):
        if self.promisedId <= m.id:
            oldId = self.promisedId
            self.promisedId = m.id
            self.network.printMsg(self.network.currentTick, m)
            if self.prior:
                newM = Message(self, m.src, 'PROMISE', self.prior, m.id, oldId)
                self.prior = None
            else:
                newM = Message(self, m.src, 'PROMISE', None, m.id)
        else:
            newM = Message(self, m.src, 'REJECTED', None, m.id)

        self.network.queueMessage(newM)

    
    def reset(self, m):
        self.network.printMsg(self.network.currentTick, str(m))
        if self.promisedId <= m.id:
            self.prior = None


    def __str__(self):
        return f'A{self.id+1}'


class Learner(Computer):
    def __init__(self, _id, network, func):
        self.value = None
        self.func = func
        self.amountLearnd = 0
        super().__init__(_id, network)

    
    def recieveMessage(self, m: Message):
        if m.type == 'SUCCES':
            self.succes(m)
        else:
            print('THIS MESSAGE TYPE IS NOT KNOWN IN LEARNER')
    

    def succes(self, m):
        self.network.printMsg(self.network.currentTick, str(m))
        self.amountLearnd += 1
        for acc in self.network.A:
            newM = Message(self, acc, 'RESET', None, m.id)
            self.network.queueMessage(newM)
        
        print(f'{self} PREDICT n={self.amountLearnd}')

        self.func(m.value)

    def __str__(self):
        return f'L{self.id+1}'