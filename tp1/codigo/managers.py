#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *

class Manager(object):
    myOnlyInstance = None
    
    def __init__(self):
        self.instances = []
    
    def initialize(self):
        self.reset()
        self.setDefaults()
        
    def reset(self):
        self.instances=[]
        
    def setDefaults(self):
        pass

    def addInstance(self,instance):
        self.instances.append(instance)
        
    def get_all(self):
        return self.instances



class Agenda(Manager):
    def __init__(self):
        super(Agenda, self).__init__()
        
    @staticmethod
    def getInstance():
        if (Agenda.myOnlyInstance is None):
            Agenda.myOnlyInstance = Agenda()
            Agenda.myOnlyInstance.initialize()
        return Agenda.myOnlyInstance
    
    
    def addContact(self, contact):
        self.instances.append(contact)
        
    def setDefaults(self):
        self.addContact(Contact(full_name='Jaimito Perez', dni=34567809, phone_number='+01186754567'))
        self.addContact(Contact(full_name='Pedro Alvarez', dni=34583923, phone_number='+01137392712'))
        self.addContact(Contact(full_name='Marina Aballay', dni=34583923, phone_number='+01143321345'))
        self.addContact(Contact(full_name='Mónica Amadore', dni=34583923, phone_number='+01120832010'))
        self.addContact(Contact(full_name='Vanesa Apicella', dni=34583923, phone_number='+01132948098'))
        self.addContact(Contact(full_name='Natalia Conde', dni=34583923, phone_number='+01133245326'))
        self.addContact(Contact(full_name='Laura De Maio', dni=34583923, phone_number='+01159328933'))
        self.addContact(Contact(full_name='Gustavo DeLorenzi', dni=34583923, phone_number='+01133363806'))
        self.addContact(Contact(full_name='María Donadio', dni=34583923, phone_number='+01136363899'))
        self.addContact(Contact(full_name='Ezequiel Donadio', dni=34583923, phone_number='+01188754646'))
        self.addContact(Contact(full_name='Juan Pablo Donadio', dni=34583923, phone_number='+01174470655'))
        self.addContact(Contact(full_name='Veronica Garcia', dni=34583923, phone_number='+01165277342'))
        self.addContact(Contact(full_name='Daiana Rios', dni=34583923, phone_number='+01122424987'))
        self.addContact(Contact(full_name='Roque Quesada', dni=34583923, phone_number='+01148052422'))
        self.addContact(Contact(full_name='Beatriz Vetere', dni=34583923, phone_number='+01135954324'))
        self.addContact(Contact(full_name='Daniel Kochian', dni=34583923, phone_number='+01179642356'))
        self.addContact(Contact(full_name='Esteban Ogando', dni=34583923, phone_number='+01133786435'))
    
       

class CourseManager(Manager):
    @staticmethod
    def getInstance():
        if (CourseManager.myOnlyInstance is None):
            CourseManager.myOnlyInstance = CourseManager()
            CourseManager.myOnlyInstance.initialize()
        return CourseManager.myOnlyInstance
    
     
    def addCourse(self, course):
        self.instances.append(course)
        
    def setDefaults(self):
        self.addCourse(Course(3,'A'))
        self.addCourse(Course(2,'B'))
        self.addCourse(Course(5,'A'))


class EventManager(Manager):
    @staticmethod
    def getInstance():
        if (EventManager.myOnlyInstance is None):
            EventManager.myOnlyInstance = EventManager()
        return EventManager.myOnlyInstance

    def addEvent(self,event):
        self.instances.append(event)

    def setDefaults(self):
        date_from = datetime(2015, 5, 30, 0, 4)
        date_to = date_from + timedelta(minutes=1)

        self.addEvent(Event('Prueba de Historia', date_from))
        self.addEvent(Event('Envío de alimentos', date_from, date_to))
        self.addEvent(Event('Envío de Geografía', date_to))
        
        
class CampaignManager(Manager):
    @staticmethod
    def getInstance():
        if (CampaignManager.myOnlyInstance is None):
            CampaignManager.myOnlyInstance = CampaignManager()
        return CampaignManager.myOnlyInstance

    def addCampaign(self,campaign):
        self.instances.append(campaign)
        
    def setDefaults(self):
        event = EventManager.getInstance().get_all()[0]
        teacher = TeacherManager.getInstance().get_all()[0]
        
        campaign = Campaign('Mejorar a los flojos en Historia', teacher, event)

        contacts = [Agenda.getInstance().get_all()[0]]
        body = 'Se tiene que mandar en seguida'
        message = Message(body, teacher, contacts)
        dateToSend = datetime(2015, 5, 30, 0, 1)
        campaign.outbox.add_message(message, dateToSend)
        
        self.addCampaign(campaign)
        
        
class TeacherManager(Manager):
    
    @staticmethod
    def getInstance():
        if (TeacherManager.myOnlyInstance is None):
            TeacherManager.myOnlyInstance = TeacherManager()
            TeacherManager.myOnlyInstance.initialize()
        return TeacherManager.myOnlyInstance
    
    def addTeacher(self,teacher):
        self.instances.append(teacher)
        
    def setDefaults(self):
        self.addTeacher(Teacher(full_name='Marcos Juarez'))
        self.addTeacher(Teacher(full_name='Pedro Troglio'))