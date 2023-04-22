from .ins import Instance
from .doc import *

class Subject(Instance):
    def __init__(self, class_type, id = None, object_number = None, object_name = None):
        super().__init__(class_type, id)
        
        for e in [object_number, object_name]:
            e = '' if e == None else None

        self.fields['object_number'] = object_number
        self.fields['object_name'] = object_name
        
    def Add(self, class_type, id = None, number = None, name = None):
        ''' 
        class_type Object: Project
        class_type Project: SpecList, EquipList, MatList, WorkList, CableList, DocList'''
        
        instance = class_type(id, number, name)
        
        if self.isSubSubinstance(class_type):
            self.add_subinstance(instance)
            return instance
        else:
           raise ValueError('Wrong instance class!')
       
    def Get(self, class_type, id = None):
        ''' 
        class_type Object: Project
        class_type Project: SpecList, EquipList, MatList, WorkList, CableList, DocList'''
        return self.get_subinstance(class_type, id)

    def Remove(self, class_type, id = None):
        ''' 
        class_type Object: Project
        class_type Project: SpecList, EquipList, MatList, WorkList, CableList, DocList'''
        self.remove_subinstance(class_type, id)

    def isSubSubinstance(self, instance_class):
        self_class = type(self)
        
        ok = False
        if self_class == Object and instance_class in [Project]:
            ok = True
        elif self_class == Project and instance_class in [SpecList, EquipList, MatList, WorkList, CableList, DocList]:
            ok = True
            
        return ok

class Object(Subject):
    def __init__(self, id = None, object_number = None, object_name = None, object_address = None):
        super().__init__(type(self), id, object_number, object_name)

        self.fields['object_address'] = object_address
        
        # self.add_subinstance(Project())  
        
    def Update(self, object_number = None, object_name = None, object_address = None):
        args = [object_number, object_name, object_address]
        for e in args:
            self.fields.update(e) if e is not None else None
    
class Project(Subject):
    ''' Проекты '''
    def __init__(self, id = None, project_number = None, project_name = None):
        super().__init__(type(self), id, project_number, project_name)

        # self.add_subinstance(SpecList())
        # self.add_subinstance(EquipList())
        # self.add_subinstance(MatList())
        # self.add_subinstance(WorkList())
        # self.add_subinstance(CableList())
        # self.add_subinstance(DocList())

    def Update(self, project_number = None, project_name = None):
        args = [project_number, project_name]
        for e in args:
            self.fields.update(e) if e is not None else None
        
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

