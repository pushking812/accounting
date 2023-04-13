from .instance import Instance

class Doc(Instance):
    def __init__(self, cls, id = None, number = None, name = None):
        super().__init__(cls, id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name

class CableLst(Doc):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)

class SpecLst(Doc):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)

class WorkLst(Doc):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)
