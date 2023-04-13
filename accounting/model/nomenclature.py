from .instance import Instance

class Nomenclature(Instance):
    def __init__(self, cls, id = None, number = None, name = None):
        super().__init__(cls, id)

        if number == None:
            number = ''

        if name == None:
            name = ''

        self.fields['number'] = number
        self.fields['name'] = name
        
class Equipment(Nomenclature):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)

class Cable(Nomenclature):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)
        
class Material(Nomenclature):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id, number, name)
        
class Cat(Instance):
    def __init__(self, id = None, number = None, name = None):
        super().__init__(type(self), id)
        
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