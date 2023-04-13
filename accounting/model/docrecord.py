from .instance import *

class DocRecord(Instance):
    def __init__(self, cls, id = None, subinstances = None, name = None):
        super().__init__(cls, id)
        
        self.fields['name'] = name

        if subinstances != None:
            for subinstance in subinstances:
                self.add_subinstance(subinstance)
                
class ObjectRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)
 
class ProjectRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

class SpecRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

class WorkLstRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

class CableJnlRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

class EquipRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

class CatRecord(DocRecord):
    def __init__(self, id = None, subinstances = None, name = None):
        super().__init__(type(self), id, subinstances, name)

