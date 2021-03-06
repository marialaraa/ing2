#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SMS import *
from clock import *
from customExceptions import CampaignNotEndedException


class Admin(object):
    def __init__(self, username):
        self.username = username


class Event(object):
    def __init__(self, name, date_from, date_to=None):
        self.name = name
        self.dateFrom = date_from
        self.dateTo = date_to
        self.campaigns = []

    def end_date(self):
        return self.dateTo if self.dateTo else self.dateFrom

    def add_campaign(self, campaign):
        self.campaigns.append(campaign)

    def get_campaigns(self):
        return [campaign for campaign in self.campaigns]

    def ended(self):
        current_time = Clock.getInstance().getCurrentTime()
        return current_time >= self.end_date()


class Campaign(object):
    def __init__(self, name, creator, event):
        self.name = name
        self.event = event
        self.creator = creator
        self.message_log = MessageLog()
        self.scheduler = Scheduler(self)
        Clock.getInstance().attach(self.scheduler)
        self.results = []
        self.event.add_campaign(self)

    def schedule_message(self, message, aDatetime):
        self.scheduler.add_message(message, aDatetime)

    def ended(self):
        return self.event.ended()

    def add_result(self, result):
        if not self.ended():
            raise CampaignNotEndedException

        self.results.append(result)

    def get_results(self):
        return [result for result in self.results]

    def getMessageLog(self):
        return self.message_log


class Result(object):
    def __init__(self, description, value):
        self.description = description
        self.value = value


class Contact(object):
    def __init__(self, full_name, dni, phone_number):
        self.fullName = full_name
        self.dni = dni
        self.phoneNumber = phone_number


class Message(object):
    def __init__(self, body, sender, adressee_list):
        self.body = body
        self.adressee_list = adressee_list
        self.sender = sender


