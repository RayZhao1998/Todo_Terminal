import time

class TodoItem():
    
    def __init__(self, title, endTime):
        self.title = title
        self.createdTime = int(time.time())
        self.endTime = endTime
        self.haveDone = False

    def Done(self):
        self.haveDone = True

    def unDone(self):
        self.haveDone = False

    def editTitle(self, newTitle):
        self.title = newTitle
        
    def editEndTime(self, newEndTime):
        self.endTime = newEndTime