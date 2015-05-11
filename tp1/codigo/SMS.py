from datetime import datetime
from managers import *
from models import *
from managers import *

class Scheduler():
    
    def __init__(self, campaign):
        self.schedule = {}
        self.campaign = campaign
        
    def reset(self):
        self.schedule={}
    
    @staticmethod
    def strf_date(date):
        return date.strftime("%H:%M:%S %d/%m/%Y")
    
    def add_message(self, message, dateToSend):
        strf_date_msg = Scheduler.strf_date(dateToSend)
        if strf_date_msg in self.schedule.keys():
            self.schedule[strf_date_msg].append(message)
        else: 
            self.schedule[strf_date_msg] = [message]
        
    def get_all(self):
        list_of_lists = [[{'message': message, 'date': key } for message in self.schedule[key]] for key in self.schedule.keys()]
        return [val for sublist in list_of_lists for val in sublist]
        
    def update(self, currentDate):
        strf_current_date = self.strf_date(currentDate)
        if strf_current_date in self.schedule.keys():
            Sender.sendAll(self.schedule[strf_current_date], self.campaign.getMessageLog())
            del self.schedule[strf_current_date]

        
class Sender(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def sendAll(msgList, message_log):
        for msg in msgList:
            message_log.addMessage(msg)


class MessageLog():

    def __init__(self):
        self.sent = []

    def addMessage(self, message):
        self.sent.append(message)

    def get_all(self):
        return self.sent