class Network():
    def __init__(self):
        self.queue = []
        self.P = []
        self.A = []
        self.currentTick = 0 # Current time, could be actual time or fictional time.
        self.proposals = 0
    

    def queueMessage(self, m):
        self.queue.append(m)
    

    def extractMessage(self):
        ret = None

        for message in self.queue:
            if not message.src.failed and not message.dst.failed:
                ret = message
                break

        if ret:
            index = self.queue.index(ret)
            del self.queue[index]

        return ret

    
    def printMsg(self, tick, msg):
        print(f'{tick:0>3}: {msg}')
        