from .instance import Instance

class Equip(Instance):
    def __init__(self, instance_id = None, equip_number = None, equip_name = None):
        super().__init__(type(self), instance_id)

        if equip_number == None:
            equip_number = ''

        if equip_name == None:
            equip_name = ''

        self.fields['equip_number'] = equip_number
        self.fields['equip_name'] = equip_name