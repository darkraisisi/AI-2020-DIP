import computer as comp


class Message():
    def __init__(self, src:comp, dst:comp, _type, value: str, id=None, priorId=None):
        self.src = src # computer verstuurder
        self.dst = dst # computer te ontvangen
        self.type = _type # PROPOSE, PREPARE, PROMISE, ACCEPT, ACCEPTED, REJECTED
        self.value = value
        self.id = id
        self.priorId = priorId

    def __str__(self):
        if self.type in ['PROPOSE', 'PREPARE', 'ACCEPT', 'ACCEPTED', 'SUCCES']:
            return f'{self.src if self.src else "  "} -> {self.dst} {self.type} {"n="+str(self.id)+" " if self.id else ""}{"v="+self.value if self.value else ""}'
        elif self.type == 'PROMISE':
            return f'{self.src if self.src else "  "} -> {self.dst} {self.type} {"n="+str(self.id) if self.id else ""} (Prior: {"n="+str(self.priorId)+" " if self.value else "None"}{"v="+self.value if self.value else ""})'
        else:
            return f'{self.src if self.src else "  "} -> {self.dst} {self.type} {"n="+str(self.id)+" " if self.id else ""}'