from clock import Clock


class ResultLoader(object):

    def __init__(self, campaign):
        Clock.getInstance().attach(self)
        self.campaign = campaign

    def update(self, a_datetime):
        if a_datetime == self.campaign.event.dateFrom:
            self.campaign.add_result('Porcentaje de aprobados', 65)