from .instance import Instance

class Spec(Instance):
    def __init__(self, instance_id = None, spec_number = None, spec_name = None):
        super().__init__(type(self), instance_id)

        if spec_number == None:
            spec_number = ''

        if spec_name == None:
            spec_name = ''

        self.fields['spec_number'] = spec_number
        self.fields['spec_name'] = spec_name


        




    
    