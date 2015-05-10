from clock import Clock


class ResultLoader(object):

    def __init__(self, campaign, result):
        Clock.getInstance().attach(self)
        self.campaign = campaign
        self.result = result

    def update(self, a_datetime):
        if a_datetime == self.campaign.event.dateFrom:
            self.campaign.add_result(self.result)
