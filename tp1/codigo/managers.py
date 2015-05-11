#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
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
        return [instance for instance in self.instances]



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
    
       

#class CourseManager(Manager):
#    @staticmethod
#    def getInstance():
#        if (CourseManager.myOnlyInstance is None):
#            CourseManager.myOnlyInstance = CourseManager()
#            CourseManager.myOnlyInstance.initialize()
#        return CourseManager.myOnlyInstance
    
     
 #  def addCourse(self, course):
 #      self.instances.append(course)
 #
 #  def setDefaults(self):
 #      self.addCourse(Course(3,'A'))
 #      self.addCourse(Course(2,'B'))
 #      self.addCourse(Course(5,'A'))


class EventManager(Manager):
    @staticmethod
    def getInstance():
        if (EventManager.myOnlyInstance is None):
            EventManager.myOnlyInstance = EventManager()
        return EventManager.myOnlyInstance

    def addEvent(self, event):
        self.instances.append(event)

    def setDefaults(self):
        
        date_exam = Clock.getInstance().getCurrentTime() + timedelta(minutes=6)
        self.addEvent(Event('Trimestral de Biología',date_exam))

        date_excu = Clock.getInstance().getCurrentTime() + timedelta(minutes=4)
        self.addEvent(Event('Excursión al comedor del Tren Blanco',date_excu))
        
        
class CampaignManager(Manager):
    @staticmethod
    def getInstance():
        if (CampaignManager.myOnlyInstance is None):
            CampaignManager.myOnlyInstance = CampaignManager()
        return CampaignManager.myOnlyInstance

    def addCampaign(self,campaign):
        self.instances.append(campaign)
        
    def setDefaults(self):
        #Prueba de Biología
        bio_event = EventManager.getInstance().get_all()[0]
        admin = AdminManager.getInstance().get_all()[0]

        campaign = Campaign('Mejorar a los flojos en Biología',admin, bio_event)

        contacts = [Agenda.getInstance().get_all()[0]][6:9]

        body = 'En tres semanas estará la trimestral de Biología. Empezar repasando los animales mamíferos. ¡Vamos que hay tiempo!'
        message = Message(body, admin, contacts)
        dateToSend = Clock.getInstance().getCurrentTime() + timedelta(minutes=2)

        body2 = 'En dos semanas estará la trimestral de Biología. Continuar repasando los animales ovíparos. ¡Último tema por aprender!'
        message2 = Message(body2, admin, contacts)
        dateToSend2 = Clock.getInstance().getCurrentTime() + timedelta(minutes=3)

        body3 = 'El próximo martes es la trimestral de Biología. Repasar la unidad uno y dos del libro. ¡Recta final!'
        message3 = Message(body3,admin,contacts)
        dateToSend3 = Clock.getInstance().getCurrentTime() + timedelta(minutes=4)

        campaign.schedule_message(message, dateToSend)
        campaign.schedule_message(message2, dateToSend2)
        campaign.schedule_message(message3, dateToSend3)

        self.addCampaign(campaign)

        campaign2 = Campaign('Avisar de la primera trimestral de Biología',admin,bio_event)

        contacts2 = [Agenda.getInstance().get_all()[0]][:5]

        body4 = 'En tres semanas estará la trimestral de Biología.'
        message4 = Message(body4, admin, contacts2)

        body5 = 'En dos semanas estará la trimestral de Biología.'
        message5 = Message(body5, admin, contacts2)

        body6 = 'El próximo martes es la trimestral de Biología.'
        message6 = Message(body6,admin,contacts2)

        campaign2.schedule_message(message4, dateToSend)
        campaign2.schedule_message(message5,dateToSend2)
        campaign2.schedule_message(message6,dateToSend3)

        self.addCampaign(campaign2)

        #Excursión Tren Blanco
        excu_event = EventManager.getInstance().get_all()[1]
        admin2 = AdminManager.getInstance().get_all()[1]
        admin3 = AdminManager.getInstance().get_all()[2]

        campaign3 = Campaign('Recordar autorización para la excursión',admin2,excu_event)

        contacts3 = [Agenda.getInstance().get_all()[0]]

        body7 = 'No olvidar de traer la autorización firmada por el padre/tutor para la visita al comedor.'
        message7 = Message(body7, admin2, contacts3)

        body8 = '¿Aún no trajiste la autorización? No te olvides de traerla mañana, sino te quedarás sin ir y te perderás de esta experiencia enriquecedora.'
        message8 = Message(body8, admin2, contacts3)

        campaign3.schedule_message(message7, dateToSend)
        campaign3.schedule_message(message8,dateToSend2)

        self.addCampaign(campaign3)

        campaign4 = Campaign('Recordar traer alimento no perecedero para la excursión',admin3,excu_event)

        body11 = 'No te olvides que mañana nos vamos de excursión al comedor del Tren Blanco. Vamos a darles una mano llevando cada uno un alimento no perecedero. Si tenes ropa o juguetes en buen estado que quieras regalarlos, podes traerlos.'
        message11 = Message(body11, admin3, contacts3)

        campaign4.schedule_message(message11,dateToSend2)

        self.addCampaign(campaign4)
        
        
class AdminManager(Manager):
    
    @staticmethod
    def getInstance():
        if (AdminManager.myOnlyInstance is None):
            AdminManager.myOnlyInstance = AdminManager()
            AdminManager.myOnlyInstance.initialize()
        return AdminManager.myOnlyInstance
    
    def addAdmin(self,admin):
        self.instances.append(admin)
        
    def setDefaults(self):
        self.addAdmin(Admin('Marcos Juarez'))
        self.addAdmin(Admin('Pedro Troglio'))
        self.addAdmin(Admin('Miriam Civitillo'))
        self.addAdmin(Admin('Estela Pavone'))