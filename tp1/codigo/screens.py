#!/usr/bin/env python
# -*- coding: utf-8 -*-
from customExceptions import InvalidInputError
from managers import *
from stringifiers import *
from clock import *
from SMS import *

class ScreenOption(object):
    
    def __init__(self, text, screenClass, screenParams=None):
        self.text = text
        self.screenClass = screenClass
        self.screenParams = screenParams
        
    def run(self):

        return self.screenClass() if not self.screenParams else self.screenClass(self.screenParams)
        
class Screen(object):
    
    
    separator = """




-----------------------------------------------------
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
-----------------------------------------------------





"""
    
    select_option_message = 'Please select an option: '
    
    def __init__(self):
        self.options = []
        
    def display_content(self):
        self.display_options()
        
    def print_time(self):
        clock = Clock.getInstance()
        time = clock.getCurrentTime().strftime("%H:%M:%S %d/%m/%Y")
        print """
        --------
        System current time: %s
        --------""" % time
        
    def display(self):
        print self.separator
        self.display_content()
        self.print_time()
        
        user_input = self.read_input()
        print self.separator
        
        return user_input
        
    def select_option(self, user_input):
        try:
            user_input = int(user_input)-1
            if user_input > -1 and user_input < len(self.options):
                return self.run_selected_option(self.options[user_input])
            else:
                raise InvalidInputError
        except ValueError, e:
            raise InvalidInputError

    def run_selected_option(self, option):
        return option.run()

    @staticmethod    
    def exit():
        return False
        
        
    def display_options(self):
        separator = '\t----'
        print(' + Options\n'+separator)
        for i in xrange(len(self.options)):
            option = self.options[i]
            print("\t("+str(i+1)+") "+option.text)
        print(separator+'\n')
        
    def read_input(self):
        invalid_input = True
        while(invalid_input):
            try:
                user_input = raw_input('\n'+self.select_option_message+'\n')
                option = self.select_option(user_input)
                invalid_input = False
            except InvalidInputError, e:
                print self.separator
                print 'Input is not a valid option'
        return option


class ExitScreen(Screen):

    @staticmethod
    def exit():
        return True

    def display(self):
        exit_message = """

              GGGG     OOOO        OOOOO    DDD
            GGG       OO  OOO      OO  OO   D DDD
           GG         O     OO   OOO     O  D   DD
          GG  GGGG    O      OO  O       O DD    D
          GG     GG   O       O  O       O D    DD
           GG     G   OO     OO  OO     OO D   DD
            GGGGGGG    OOOOOOO    OOOOOOO  DDDDD


               BBBBB     Y    YY  EEEEEE
               B   BB     Y   Y   E
               B  BBB      Y Y    EEEEE
               BBBBBBB      YY    E
               B     B     YY     E
              BBB  BBB   YYY      EEEEEE
              B BBBB     Y
             """
        print exit_message
        return self
        
class HomeScreen(Screen):
    
    def __init__(self):
        super(HomeScreen, self).__init__()
        list_contacts_option = ScreenOption("View agenda", ListContactsScreen)
        self.options.append(list_contacts_option)
        list_campaigns_option = ScreenOption("List events", ListEventsScreen)
        self.options.append(list_campaigns_option)
        add_a_minute_option = ScreenOption("Add a minute", AddMinuteScreen)
        self.options.append(add_a_minute_option)
        self.options.append(ScreenOption("Exit", ExitScreen))
        
    def display_content(self):
        welcome_message = """
           AA                                                             
          AAAA      U      U   L            A                             
         AA  A      U      U   L           AAA
         A   A      U      U   L          AA AA                           
        AA    A     U      U  LL         AA   A                           
        AAAAAAAAA    U    UU  L          A    A                           
        A     AA     UU  UU   L        AAAAAAAAA                          
       AA      A      UUUU    LLLLLLL  A      A                           
                                      AA      A                           
                                222                                       
         22222        0000    222 22      0000                            
       22    2       00  00  22    2     0   00                           
            22       0    00       2    0     00                          
           22        0     0       2   00      00                         
          22         0     0      22   0        0                         
         2           0     0      2    0        0                         
        2            0     0     2     0       00                         
        2222222222   0000000    22     00     00                          
                        00     2222222  0000000        
"""
        print(welcome_message)
        super(HomeScreen, self).display_content()


class ListScreen(Screen):
    
    model = None
    modelName = None
    modelManager = None
    modelStringifier = Stringifier
    
    def __init__(self):
        super(ListScreen, self).__init__()
        
    def display_content(self):
        instances = self.get_instances()
        print '/******/\n%s:\n' % self.modelName
        str_list =  '\n'.join([ '\t'+self.display_item(instance) for instance in instances])
        print str_list
        print '\n/******/\n'
        super(ListScreen, self).display_content()

    def display_item(self, item):
        return self.modelStringifier(item).to_string()

    def get_instances(self):
        return self.modelManager.get_all()


class ListContactsScreen(ListScreen):
    
    model = Contact
    modelName = 'Agenda'
    modelManager = Agenda.getInstance()
    modelStringifier = ContactStringifier
    
    def __init__(self):
        super(ListContactsScreen, self).__init__()
        back_to_home_option = ScreenOption("Back to home", HomeScreen)
        self.options.append(back_to_home_option)


class ListEventsScreen(ListScreen):
    model = Event
    modelName = 'Event'
    modelManager = EventManager.getInstance()
    modelStringifier = EventStringifier
    
    def __init__(self):
        super(ListEventsScreen, self).__init__()
        events = EventManager.getInstance().get_all()
        for event in events:
            s = EventStringifier(event).to_string()
            event_option = ScreenOption("View %s" % s, ListCampaignsScreen,event)
            self.options.append(event_option)
        back_to_home_option = ScreenOption("Back to home", HomeScreen)
        self.options.append(back_to_home_option)

    def display_item(self, event):
        campaigns = '\n\t\t'.join([CampaignStringifier(campaign).to_string() for campaign in event.get_campaigns()])
        return EventStringifier(event).to_string() + '\n\t\t[%s]' % campaigns


class ListCampaignsScreen(ListScreen):

    model = Campaign
    modelName = 'Campaigns'
    modelManager = CampaignManager.getInstance()
    modelStringifier = CampaignStringifier

    def display_content(self):
        print 'Campaigns for %s' % EventStringifier(self.event).to_string()
        super(ListCampaignsScreen, self).display_content()

    def __init__(self, event):
        super(ListCampaignsScreen, self).__init__()
        self.event = event
        campaigns = self.get_instances()
        for campaign in campaigns:
            s = CampaignStringifier(campaign)
            campaign_option = ScreenOption("View %s" % s.to_string(), ShowCampaignScreen, campaign)
            self.options.append(campaign_option)
        back_to_home_option = ScreenOption("Back to events", ListEventsScreen)
        self.options.append(back_to_home_option)

    def get_instances(self):
        return self.event.campaigns


class ListSentMessagesScreen(ListScreen):
    
    model = Message
    modelName = 'Sent Messages'
    modelStringifier = MessageStringifier
    
    def __init__(self, campaign):
        super(ListSentMessagesScreen, self).__init__()
        back_to_campaign_option = ScreenOption("Back to campaign", ShowCampaignScreen, campaign)
        self.options.append(back_to_campaign_option)
        self.modelManager = campaign.sent_messages
    
class ListMessagesToSendScreen(ListScreen):
    
    model = Message
    modelName = 'Messages to Send'
    modelStringifier = MessageToSendStringifier
    
    def __init__(self, campaign):
        super(ListMessagesToSendScreen, self).__init__()
        back_to_campaign_option = ScreenOption("Back to campaign", ShowCampaignScreen, campaign)
        self.options.append(back_to_campaign_option)
        self.modelManager = campaign.outbox


class ListResultsScreen(ListScreen):

    model = Result
    modelName = 'Results'
    modelStringifier = ResultStringifier

    def __init__(self, campaign):
        super(ListResultsScreen, self).__init__()
        back_to_campaign_option = ScreenOption("Back to campaign", ShowCampaignScreen, campaign)
        self.options.append(back_to_campaign_option)
        self.campaign = campaign

    def get_instances(self):
        return self.campaign.get_results()

    
class AddMinuteScreen(Screen):
    
    def __init__(self):
        super(AddMinuteScreen, self).__init__()
        back_to_home_option = ScreenOption("Add another minute", AddMinuteScreen)
        self.options.append(back_to_home_option)
        back_to_home_option = ScreenOption("Back to home", HomeScreen)
        self.options.append(back_to_home_option)
        Clock.getInstance().add_a_minute()
        
    def display_content(self):
        print "A minute was added to the current time"
        super(AddMinuteScreen, self).display_content()


class ShowCampaignScreen(Screen):
    def __init__(self, campaign):
        self.campaign = campaign
        super(ShowCampaignScreen, self).__init__()
        list_outbox_messages_option = ScreenOption("List outbox messages", ListMessagesToSendScreen,campaign)
        self.options.append(list_outbox_messages_option)
        list_sent_messages_option = ScreenOption("List sent messages", ListSentMessagesScreen,campaign)
        self.options.append(list_sent_messages_option)
        if campaign.ended():
            list_results_option = ScreenOption("List results", ListResultsScreen,campaign)
            self.options.append(list_results_option)
        back_to_capaigns_option = ScreenOption("Back to event view", ListCampaignsScreen, self.campaign.event)
        self.options.append(back_to_capaigns_option)
        
    def display_content(self):
        s = CampaignStringifier(self.campaign)
        print '\nCAMPAIGN: %s\n\n' % s.to_string()
        super(ShowCampaignScreen, self).display_content()