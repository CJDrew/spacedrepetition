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
        self.repNum = 1
        self.addedDate = datetime.datetime.now()
        self.lastDoneDate = datetime.datetime.now()
    
    def isDue(self) -> bool:
        if self.isDone():
            raise Exception("End of schedule")
        nextDueDate = self.addedDate + datetime.timedelta(days=self.schedule[self.repNum]) 
        return self.lastDoneDate < nextDueDate and datetime.datetime.now() >= nextDueDate

    def isDone(self) -> bool:
        return self.repNum > len(self.schedule)

    def addRepetition(self) -> None:
        self.repNum += 1
        self.lastDoneDate = datetime.datetime.now()