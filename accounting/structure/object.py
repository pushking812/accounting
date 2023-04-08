from .instance import Instance

class Object(Instance):
    def __init__(self, instance_id = None, object_number = None, object_name = None):
        super().__init__(type(self), instance_id)
        
        if object_number == None:
            object_number = ''

        if object_name == None:
            object_name = ''

        self.fields['object_number'] = object_number
        self.fields['object_name'] = object_name