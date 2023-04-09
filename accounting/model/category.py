from .instance import Instance

class Cat(Instance):
    def __init__(self, instance_id = None, cat_number = None, cat_name = None):
        super().__init__(type(self), instance_id)
        
        if cat_number == None:
            cat_number = ''

        if cat_name == None:
            cat_name = ''

        self.fields['cat_number'] = cat_number
        self.fields['cat_name'] = cat_name

        # if cat_numbers == None:
        #     cat_numbers = []

        # if cat_name == None:
        #     cat_name = ''
        
        # for i in range(len(cat_numbers)):
        #     self.fields[f'cat{i}_number'] = cat_numbers[i]
            
        # self.fields[f'cat_name'] = cat_name

        # level = str(type(cls).__name__)[-1] 

        # if not level.isdigit(level):
        #     raise ValueError("Last symbol must be digit")
        
        # if len(cat_numbers) != (level+1):
        #     raise ValueError("Wrong number of categories")

        # Cat.category_level_max = level if level > Cat.category_level_max else None

        # 
        

        

