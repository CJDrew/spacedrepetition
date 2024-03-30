import datetime

class problem:
    schedule = {
        1: 1,
        2: 3,
        3: 7,
        4: 21,
        5: 30,
        6: 45,
        7: 60
    }

    def __init__(self, id):
        self.id = id
        self.repNum = 0
        self.addedDate = datetime.datetime.now()
        self.lastDoneDate = datetime.datetime.now()
    
    def isDue(self) -> bool:
        nextDueDate = self.addedDate + datetime.timedelta(days=self.schedule[self.repNum+1]) 
        return self.lastDoneDate < nextDueDate and datetime.datetime.now >= nextDueDate