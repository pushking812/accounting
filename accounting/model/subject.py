from .instance import Instance

class Object(Instance):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)
        
        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name
        
        # self.subinstances['Project']=Project(0, 'root', 'root')

class Project(Instance):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name       

class Work(Instance):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name