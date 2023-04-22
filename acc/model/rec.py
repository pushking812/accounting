from .ins import *
from .doc import *
from .nom import *


class Record(Instance):
    def __init__(self, instance_class, id = None, rec_number = None, rec_name = None, rec_value = None):
        super().__init__(instance_class, id)
        
        for e in [rec_number, rec_name, rec_value]:
            e = '' if e == None else None
                
        self.fields['rec_number'] = rec_number
        self.fields['rec_name'] = rec_name
        self.fields['rec_value'] = rec_value

class SpecRecord(Record):
    def __init__(self, instance_class = None, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_field1 = None, rec_field2 = None):

        if instance_class == None:
            instance_class = type(self)
        
        super().__init__(instance_class, id, rec_number, rec_name, rec_value)
            
        self.fields['rec_field1'] = rec_field1
        self.fields['rec_field2'] = rec_field2
        

                
class EquipRecord(SpecRecord):
    def __init__(self, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_field3 = None, rec_field4 = None):
        super().__init__(type(self), id, rec_number, rec_name, rec_value)
        
        self.fields['rec_field3'] = rec_field3
        self.fields['rec_field4'] = rec_field4
        
        self.add_subinstance(Equipment())

class MatRecord(SpecRecord):
    def __init__(self, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_field5 = None, rec_field6 = None):
        super().__init__(type(self), id, rec_number, rec_name, rec_value)
        
        self.fields['rec_field5'] = rec_field5
        self.fields['rec_field6'] = rec_field6

        self.add_subinstance(Material())
        
class WorkRecord(SpecRecord):
    def __init__(self, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_field1 = None, rec_field2 = None):
        super().__init__(type(self), id, rec_number, rec_name, rec_value)
        
        self.fields['rec_field1'] = rec_field1
        self.fields['rec_field2'] = rec_field2

        self.add_subinstance(EquipRecord())        
        self.add_subinstance(MatRecord())
        self.add_subinstance(CableRecord())

class CableRecord(Record):
    def __init__(self, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_value1 = None, rec_value2 = None, rec_startat = None, rec_endat = None):
        super().__init__(type(self), id, rec_number, rec_name, rec_value)
        
        self.fields['rec_startat'] = rec_startat
        self.fields['rec_endat'] = rec_endat
        self.fields['rec_value1'] = rec_value1
        self.fields['rec_value2'] = rec_value2
        
        self.add_subinstance(Cable())       
    
class DocRecord(Record):
    def __init__(self, id = None, rec_number = None, rec_name = None, rec_value = None, 
                 rec_revision = None, rec_format = None):
        super().__init__(type(self), id, rec_number, rec_name, rec_value)
        
        self.fields['rec_format'] = rec_revision
        self.fields['rec_revision'] = rec_format
 