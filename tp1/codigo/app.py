#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from managers import *
from screens import *
from customExceptions import *
import datetime
from resultloader import ResultLoader
from utils import clear


class App(object):
    def __init__(self):
        self.clock = Clock.getInstance()
        self.currentScreen = HomeScreen()
        self.agenda = Agenda.getInstance()
        self.agenda.initialize()
        EventManager.getInstance().setDefaults()
        CampaignManager.getInstance().setDefaults()
        ResultLoader(CampaignManager.getInstance().get_all()[0], Result('Porcentaje de alumnos flojos aprobados',65))
        ResultLoader(CampaignManager.getInstance().get_all()[1], Result('Porcentaje de alumnos responsables aprobados',80))
        ResultLoader(CampaignManager.getInstance().get_all()[2], Result('Porcentaje de alumnos que trajeron la autorización',90))
        ResultLoader(CampaignManager.getInstance().get_all()[3], Result('Porcentaje de alumnos que trajeron el alimento no perecedero',80))

    def run(self):
        clear()
        while not self.currentScreen.exit():
            self.currentScreen = self.currentScreen.display()
            clear()
        self.currentScreen.display()