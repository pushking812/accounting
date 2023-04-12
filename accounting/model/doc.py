from .instance import Instance

class Doc(Instance):
    def __init__(self, cls, instance_id = None, number = None, name = None):
        super().__init__(cls, instance_id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name

class CableLst(Doc):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id, name)

class SpecLst(Doc):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id, name)

class WorkLst(Doc):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id, name)
