from datetime import datetime, timedelta

class Clock(object):
    
    instance = None
    
    @staticmethod
    def getInstance():
        if not Clock.instance:
            Clock.instance = Clock(datetime(2015, 5, 30, 0, 0))
        return Clock.instance
    
    def __init__(self, aTime=datetime.now()):
        self.observers = set()
        self.currentTime = aTime
        
    def attach(self, observer):
        self.observers.add(observer)
    
    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self.currentTime)
            
    def add_a_minute(self):
        self.add_time(timedelta(minutes=1))
        
    def add_time(self, aTimeDelta):
        self.currentTime += aTimeDelta
        self.notify()
        
    def getCurrentTime(self):
        return self.currentTime