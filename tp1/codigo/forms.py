

class Form(object):
    
    #######################################################
    class Field(object):
        value = None
        def set_value(self):
            raise NotImplementedError
    
    class Textfield(Field):
        pass
    
    class SelectField(Field):
        options = []
        
        def add_option(self, option):
            self.options.append(option)
            
        def get_options(self):
            return self.options
        
    #######################################################
    
    fields = []
    
    def add_field(self, field):
        self.fields.append(field)
        
    def submit(self):
        pass
    
    def read_input(self):
        pass