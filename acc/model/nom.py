from .ins import Instance

class Nom(Instance):
    def __init__(self, cls, id = None, nom_number = None, nom_name = None, 
                 cat_instance = None, unit_instance = None):
        super().__init__(cls, id)

        for e in [nom_number, nom_name]:
            e = '' if e == None else None

        self.fields['nom_number'] = nom_number
        self.fields['nom_name'] = nom_name
        
        instances = {Category: cat_instance, Unit: unit_instance,}
       
        for class_type, parameter in instances.items():
            if parameter != None:
                if not isinstance(parameter, class_type):
                    raise ValueError(f'Instance {parameter} isn\'t {class_type} type!')
        
class Equipment(Nom):
    def __init__(self, id = None, eqp_number = None, eqp_name = None, 
                 cat_instance = None, unit_instance = None):
        super().__init__(type(self), id, eqp_number, eqp_name, cat_instance, unit_instance)
        
class Material(Nom):
    def __init__(self, id = None, mat_number = None, material_name = None, 
                 cat_instance = None, unit_instance = None):
        super().__init__(type(self), id, mat_number, material_name, cat_instance, unit_instance)

class Work(Nom):
    def __init__(self, id = None, cab_number = None, cab_name = None, 
                 cat_instance = None, unit_instance = None):
        super().__init__(type(self), id, cab_number, cab_name, cat_instance, unit_instance)

class Cable(Nom):
    def __init__(self, id = None, cab_number = None, cab_name = None, 
                 cat_instance = None, unit_instance = None):
        super().__init__(type(self), id, cab_number, cab_name, cat_instance, unit_instance)
        
class Category(Instance):
    def __init__(self, id = None, cat_number = None, cat_name = None):
        super().__init__(type(self), id)
        
        for e in [cat_number, cat_name]:
            e = '' if e == None else None

        self.fields['cat_number'] = cat_number
        self.fields['cat_name'] = cat_name

class Unit(Instance):
    def __init__(self, id = None, unt_name = None):
        super().__init__(type(self), id)

        if unt_name == None:
            unt_name = ''

        self.fields['unt_name'] = unt_name