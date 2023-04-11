from .instance import Instance

class Nomenclature(Instance):
    def __init__(self, cls, instance_id = None, number = None, name = None):
        super().__init__(cls, instance_id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name
        
class Equipment(Nomenclature):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)

class Cable(Nomenclature):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)
        
class Material(Nomenclature):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)
        
class Cat(Instance):
    def __init__(self, instance_id = None, number = None, name = None):
        super().__init__(type(self), instance_id)
        
        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name

        # if cat_numbers == None:
        #     cat_numbers = []

        # if name == None:
        #     name = ''
        
        # for i in range(len(cat_numbers)):
        #     self.fields[f'cat{i}_number'] = cat_numbers[i]
            
        # self.fields[f'name'] = name

        # level = str(type(cls).__name__)[-1] 

        # if not level.isdigit(level):
        #     raise ValueError("Last symbol must be digit")
        
        # if len(cat_numbers) != (level+1):
        #     raise ValueError("Wrong number of categories")

        # Cat.category_level_max = level if level > Cat.category_level_max else None

        # 