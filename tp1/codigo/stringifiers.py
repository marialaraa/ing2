#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *


class Stringifier(object):
    def __init__(self, instance):
        self.instance = instance

    def to_string(self):
        raise NotImplementedError


class ContactStringifier(Stringifier):
    def to_string(self):
        name = self.instance.fullName
        number = self.instance.phoneNumber
        doc = self.instance.dni
        return name + '(DNI:' + str(doc) + '): ' + str(number)


class CampaignStringifier(Stringifier):
    def to_string(self):
        name = self.instance.name
        event = self.instance.event
        creator = self.instance.creator
        creator_str = ManagerStringifier(creator).to_string()
        ended_str = '(ENDED)' if self.instance.ended else ''
        return '"%s" by "%s %s"' % (name, creator_str, ended_str)


class EventStringifier(Stringifier):
    def to_string(self):
        name = self.instance.name
        date_from = str(self.instance.dateFrom)
        date_to = ' - ' + str(self.instance.dateTo) if self.instance.dateTo else ''
        return name + '(' + date_from + date_to + ')'


class ManagerStringifier(Stringifier):
    def to_string(self):
        return 'Manager: ' + str(self.instance.username)


class MessageStringifier(Stringifier):
    def to_string(self):
        sms_from = ManagerStringifier(self.instance.sender).to_string()
        sms_to = '[%s]' % ", ".join(
            [ContactStringifier(contact).to_string() for contact in self.instance.adressee_list])
        sms_body = self.instance.body
        return 'SMS From: "%s" to: %s body: "%s"' % (sms_from, sms_to, sms_body)


class MessageToSendStringifier(Stringifier):
    def to_string(self):
        date_to_send = self.instance['date']
        message = MessageStringifier(self.instance['message']).to_string()
        return 'Date: %s SMS: %s' % (date_to_send, message)


class ResultStringifier(Stringifier):
    def to_string(self):
        description = self.instance.description
        value = str(self.instance.value)
        return '%s: %s' % (description, value)