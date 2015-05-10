EventManager
def setDefaults(self):
        date_from = datetime.datetime.now()
        date_exam = date_from.replace(day=date_from.day + 6)
        self.addEvent(Event('Prueba de Biología',date_exam))
        
        date_excu = date_from.replace(day=date_from.dat + 4)
        self.addEvent(Event('Excursión al comedor del Tren Blanco',date_to))
        
        
TeacherManager
def setDefaults(self):
        self.addTeacher(Teacher(full_name='Miriam Civitillo'))
        self.addTeacher(Teacher(full_name='Estela Pavone'))

Agenda
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
    
CampaignManager
def setDefaults(self):
        #Prueba de Biología
        teacherManager = TeacherManager.getInstance()
        teacher = TeacherManager.getInstance().get_all()[0]
        
        campaign = Campaign('Mejorar a los flojos en Biología',teacher)
        
        contacts = [Agenda.getInstance().get_all()[0]][6:9]

        body = 'En tres semanas estará la trimestral de Biología. Empezar repasando los animales mamíferos. ¡Vamos que hay tiempo!'
        message = Message(body, teacher, contacts)
        dateToSend = datetime(2015, 5, 30, 0, 2)
        
        body2 = 'En dos semanas estará la trimestral de Biología. Continuar repasando los animales ovíparos. ¡Último tema por aprender!'
        message2 = Message(body2, teacher, contacts)
        dateToSend2 = datetime(2015, 5, 30, 0, 3)
        
        body3 = 'El próximo martes es la trimestral de Biología. Repasar la unidad uno y dos del libro. ¡Recta final!'
        message3 = Message(body3,teacher,contacts)
        dateToSend3 = datetime(2015, 5, 30, 0, 4)
        
        campaign.messages_to_send.addAMessage(message, dateToSend)
        campaign.messages_to_send.addAMessage(message2,dateToSend2)
        campaign.messages_to_send.addAMessage(message3,dateToSend3)
        
        self.addCampaign(campaign)

        campaign2 = Campaign('Avisar de la primera trimestral de Biología',teacher)
        
        contacts2 = [Agenda.getInstance().get_all()[0]][:5]

        body4 = 'En tres semanas estará la trimestral de Biología.'
        message4 = Message(body4, teacher, contacts2)
        
        body5 = 'En dos semanas estará la trimestral de Biología.'
        message5 = Message(body5, teacher, contacts2)
        
        body6 = 'El próximo martes es la trimestral de Biología.'
        message6 = Message(body6,teacher,contacts2)
        
        campaign.messages_to_send.addAMessage(message4, dateToSend)
        campaign.messages_to_send.addAMessage(message5,dateToSend2)
        campaign.messages_to_send.addAMessage(message6,dateToSend3)
        
        self.addCampaign(campaign2)

        #Excursión Tren Blanco
        teacher2 = TeacherManager.getInstance().get_all()[1]
        
        campaign3 = Campaign('Recordar autorización para la excursión',teacher)
        
        contacts3 = [Agenda.getInstance().get_all()[0]]

        body7 = 'No olvidar de traer la autorización firmada por el padre/tutor para la visita al comedor.'
        message7 = Message(body7, teacher2, contacts3)
        
        body8 = '¿Aún no trajiste la autorización? No te olvides de traerla mañana, sino te quedarás sin ir y te perderás de esta experiencia enriquecedora.'
        message8 = Message(body8, teacher2, contacts3)
        
        campaign3.messages_to_send.addAMessage(message7, dateToSend)
        campaign3.messages_to_send.addAMessage(message8,dateToSend2)
        
        self.addCampaign(campaign3)

        campaign4 = Campaign('Recordar traer alimento no perecedero para la excursión',teacher)
        
        body11 = 'No te olvides que mañana nos vamos de excursión al comedor del Tren Blanco. Vamos a darles una mano llevando cada uno un alimento no perecedero. Si tenes ropa o juguetes en buen estado que quieras regalarlos, podes traerlos.'
        message11 = Message(body11, teacher2, contacts3)
        
        campaign4.messages_to_send.addAMessage(message11,dateToSend2)
        
        self.addCampaign(campaign4)

