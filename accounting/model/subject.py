from .instance import Instance

class Object(Instance):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id)
        
        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name
        
        # self.subinstances['Project']=Project(0, 'root', 'root')
        
class Project(Instance):
    ''' справочник проектов '''
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name      

    # @classmethod
    # def new_instance(cls, number = None, name = None):
    #     ''' новый проект '''
    #     return cls(**{'id': None, 'number': number, 'name': name})

    # @classmethod
    # def remove_instance(cls, number = None, name = None, instance = None):
    #     ''' удалить проект '''
    #     if number is not None:
    #         del project
        
    #     if name is not None:
    #         del project
        
    #     if instance is not None:
    #         del project

    # @classmethod
    # def update_instance(cls, number = None, name = None):
    #     ''' обновить данные проекта '''
    #     pass  

class Work(Instance):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name