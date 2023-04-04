class Instance:
    instances = []

    def __init__(self, cls, numb, name):
        Instance.instances.append(self)
        self.fields = {'class': cls.__name__, 'numb': numb, 'name': name}
        self.subinsts = {}

    def add_subinst(self, i):
        key = type(i).__name__
        if key not in self.subinsts:
            self.subinsts[key] = []
        self.subinsts[key].append(i)

    def get_subinsts(self, key):
        if key not in self.subinsts:
            return []
        return self.subinsts[key]

    @classmethod
    def add_field(cls, value, key):
        for instance in cls.instances:
            if isinstance(instance, cls):
                instance.fields[key] = value

    @classmethod
    def get_instances(cls):
        result = []
        for ins in cls.instances:
            for property_name, value in ins.__dict__.items():
                if isinstance(ins, cls):
                    result.append([property_name, value])
        return result


class Object(Instance):
    def __init__(self, numb, name):
        super().__init__(type(self), numb, name)


class Project(Instance):
    def __init__(self, numb, name):
        super().__init__(type(self), numb, name)


class Spec(Instance):
    def __init__(self, numb, name):
        super().__init__(type(self), numb, name)

class Record(Instance):
    def __init__(self, cls, numb, name):
        super().__init__(cls, numb, name)
 
class SpecRecord(Record):
    def __init__(self, numb, name, value = None, equip = None):
        super().__init__(type(self), numb, name)

        if equip == None:
            equip = Equip(**{'numb': 'None', 'name': 'None'})
        self.add_subinst(equip)
        
        if value == None:
            self.fields['value'] = 0

class Equip(Instance):
    def __init__(self, numb, name):
        super().__init__(type(self), numb, name)


object = Object(**{'numb': 'O1', 'name': 'O1N'})

object.add_subinst(Project(**{'numb': 'P1', 'name': 'P1N'}))
project1 = object.get_subinsts('Project')[0]

project1.add_subinst(Spec(**{'numb': 'S1', 'name': 'S1N'}))
spec1 = project1.get_subinsts('Spec')[0]

equip1 = Equip(**{'numb': 'E1', 'name': 'E1N'})

# spec1.add_subinst(Record(**{'numb': 'R1', 'name': 'R1N', 'value': 100, 'equip': equip1}))
spec1.add_subinst(SpecRecord(**{'numb': 'R1', 'name': 'R1N'}))
rec1 = spec1.get_subinsts('SpecRecord')[0]

print(SpecRecord.get_instances())
