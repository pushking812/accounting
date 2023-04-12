from .instance import *

class DocRecord(Instance):
    def __init__(self, cls, instance_id = None, subinstances = None, name = None):
        super().__init__(cls, instance_id)
        
        self.fields['name'] = name

        if subinstances != None:
            for subinstance in subinstances:
                self.add_subinstance(subinstance)
                
class ObjectRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)
 
class ProjectRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

class SpecRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

class WorkLstRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

class CableJnlRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

class NomRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

class CatRecord(DocRecord):
    def __init__(self, instance_id = None, subinstances = None, name = None):
        super().__init__(type(self), instance_id, subinstances, name)

