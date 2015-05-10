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
        self.currentScreen = HomeScreen()
        self.agenda = Agenda.getInstance()
        self.agenda.initialize()
        self.clock = Clock.getInstance()
        EventManager.getInstance().setDefaults()
        CampaignManager.getInstance().setDefaults()
        # CourseManager.initialize()
        # TeacherManager.initialize()
        # AssignManager.initialize()
        self.result_loader = ResultLoader(CampaignManager.getInstance().get_all()[0])

    def run(self):
        clear()
        while not self.currentScreen.exit():
            self.currentScreen = self.currentScreen.display()
            clear()
        self.currentScreen.display()