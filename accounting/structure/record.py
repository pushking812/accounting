from .instance import *

class Record(Instance):
    def __init__(self, cls, instance_id = None, subinstances = None, commentary = None):
        super().__init__(cls, instance_id)

        if commentary == None:
            commentary = ''
        
        self.fields['commentary'] = commentary

        if subinstances != None:
            for subinstance in subinstances:
                self.add_subinstance(subinstance)

class ObjectRecord(Record):
    def __init__(self, instance_id = None, subinstances = None, commentary = None):
        super().__init__(type(self), instance_id, subinstances, commentary)
 
class ProjectRecord(Record):
    def __init__(self, instance_id = None, subinstances = None, commentary = None):
        super().__init__(type(self), instance_id, subinstances, commentary)