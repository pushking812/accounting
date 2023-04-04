# Приложение на Python. Предназначено для организации хранения связанных между собой данных.
# Для указанной задачи используется набор классов. Экземпляры классов имеют два основных свойства 
# хранящих данные в виде словарей: свойство fields с конечными данные экземпляра и свойство 
# subinstances содержащее список экземпляров классов связанных с данным экземпляром.
# Приложение имеет возможность сохранять и загружать данные хранящиеся в свойстве fields
# каждого класса в формате эксель (используя библиотеку openpyxl). Для сохранения связей с дочерними
# экземлярами хранящимися в свойстве subinstances, используется ключ 'id_by_class' свойства field, 
# хранящий индивидуальный номер каждого экземпляра в пределах отдельного класса.
# При сохранении данных в файл, если файл не существует, то он создается. Для каждого класса 
# создается отдельный лист с названием соответствующим названию класса. В таблицах листов сохраняются 
# элементы словарей fields всех экземпляров соответствующего класса, где ключи словарей соответствуют 
# названиям столбцов, а значения элементов словарей являются записями таблицы. Номер 'id_by_class' 
# экземпляров классов хранящегося в subinstances сохраняется в столбце с названием класса хранящегося 
# элемента с добавлением к названию постфикса '_instance'. При чтении из файла с листа соответствующего
# класса считывается данные его экземпляров. Для этого открывается лист с соответствующим классу 
# названием, для каждой записи таблицы создается экземпляр класса и в его свойство fields сохраняются 
# данные из столбцов с названиями без постфикса '_instance'.

# Я не понимаю, как организовать загрузку данных из файла. Проблема в том, что предполагается загрузка 
# экземпляров по классам, а при загрузке столбцы с id_by_class классов могут содержать ссылки на еще не 
# созданные экземпляры, но которые могут быть загружены далее.

# Примерная структура данных:


class Instance:
    instances = []

    def __init__(self, cls, numb, name):
        Instance.instances.append(self)
        self.fields = {'class': cls.__name__, 'numb': numb, 'name': name}
        self.subinsts = {}

    @classmethod
    def add_field(cls, value, key):
        for instance in cls.instances:
            if isinstance(instance, cls):
                instance.fields[key] = value

    @classmethod
    def get_fields(cls, key):
        result=[]
        result.append(key)
        for instance in cls.instances:
            if isinstance(instance, cls):
                 if key in instance.fields:
                    result.append(instance.fields[key])
        return result
    
    @classmethod
    def get_instances(cls):
        result=[]
        for ins in cls.instances:
            for property_name, value in ins.__dict__.items():
                if isinstance(ins, cls):
                    result.append([property_name, value])
        return result

    def add_subinst(self, i):
        key = type(i).__name__
        if key not in self.subinsts:
            self.subinsts[key] = []
        self.subinsts[key].append(i)

    def get_subinsts(self, key):
        if key not in self.subinsts:
            return []
        return self.subinsts[key]

    def traverse_properties(self, depth=None):
        print(f"---------------------------")
        print(f"Instance '{self.fields['name']}' of class {self.__class__.__name__}:")
        if depth is None or depth > 0:
            for property_name, value in self.__dict__.items():
                if property_name == 'subinsts':
                    for key, subinst_list in value.items():
                        print(f"{key} (list of {key})")
                        for subinst in subinst_list:
                            subinst.traverse_properties(
                                depth=depth-1 if depth is not None else None)
                else:
                    print(property_name, value)
                    if hasattr(value, '__dict__'):
                        value.traverse_properties(
                            depth=depth-1 if depth is not None else None)

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

object = Object(**{'numb': 'O1', 'name': 'Object1'})

projects_data = [
    {'numb': 'P1', 'name': 'Project1'},
    {'numb': 'P2', 'name': 'Project2'},
    {'numb': 'P3', 'name': 'Project3'}
]

for pd in projects_data:
    object.add_subinst(Project(**pd))

specs_data = [
    {'numb': 'N1', 'name': 'Spec1'},
    {'numb': 'N2', 'name': 'Spec2'},
    {'numb': 'N3', 'name': 'Spec3'},
    {'numb': 'N4', 'name': 'Spec4'},
    {'numb': 'N5', 'name': 'Spec5'},
    {'numb': 'N6', 'name': 'Spec6'}
]

projects=object.get_subinsts('Project')
i = 1
for sd in specs_data:
    if i % 3 == 1:
        projects[0].add_subinst(Spec(**sd))
    if i % 3 == 2:
        projects[1].add_subinst(Spec(**sd))
    if i % 3 == 0:
        projects[2].add_subinst(Spec(**sd))
    i=i+1

equip_data = [
    {'numb': 'E1', 'name': 'Equip1'},
    {'numb': 'E2', 'name': 'Equip2'},
    {'numb': 'E3', 'name': 'Equip3'},
    {'numb': 'E4', 'name': 'Equip4'},
    {'numb': 'E5', 'name': 'Equip5'},
    {'numb': 'E6', 'name': 'Equip6'},
    {'numb': 'E7', 'name': 'Equip7'},
    {'numb': 'E8', 'name': 'Equip8'}
]

spec_recs_data = [
    {'numb': 1, 'name': '', 'value': 100.0, 'equip': Equip(**equip_data[0])},
    {'numb': 2, 'name': '', 'value': 200.0, 'equip': Equip(**equip_data[1])},
    {'numb': 1, 'name': '', 'value': 300.0, 'equip': Equip(**equip_data[2])},
    {'numb': 2, 'name': '', 'value': 100.0, 'equip': Equip(**equip_data[3])},
    {'numb': 1, 'name': '', 'value': 200.0, 'equip': Equip(**equip_data[4])},
    {'numb': 2, 'name': '', 'value': 300.0, 'equip': Equip(**equip_data[5])},
    {'numb': 1, 'name': '', 'value': 300.0, 'equip': Equip(**equip_data[0])},
    {'numb': 2, 'name': '', 'value': 100.0, 'equip': Equip(**equip_data[1])},
    {'numb': 1, 'name': '', 'value': 200.0, 'equip': Equip(**equip_data[2])},
    {'numb': 2, 'name': '', 'value': 300.0, 'equip': Equip(**equip_data[3])},
    {'numb': 1, 'name': '', 'value': 100.0, 'equip': Equip(**equip_data[4])},
    {'numb': 2, 'name': '', 'value': 200.0, 'equip': Equip(**equip_data[5])}
]

specs=[]
i=0
for p in projects:
    for s in p.get_subinsts('Spec'):
        specs.append(s)

i = 1
for sd in spec_recs_data:
    if i % 6 == 1:
        specs[0].add_subinst(SpecRecord(**sd))
    if i % 6 == 2:
        specs[1].add_subinst(SpecRecord(**sd))
    if i % 6 == 3:
        specs[2].add_subinst(SpecRecord(**sd))
    if i % 6 == 4:
        specs[3].add_subinst(SpecRecord(**sd))
    if i % 6 == 5:
        specs[4].add_subinst(SpecRecord(**sd))
    if i % 6 == 0:
        specs[5].add_subinst(SpecRecord(**sd))
    i=i+1

# specs[0].traverse_properties(2)

recs=[]
for s in specs:
    for r in s.get_subinsts('Record'):
        recs.append(r)

equips=[]
for r in recs:
    for e in r.get_subinsts('Record'):
        recs.append(e)

for eq in SpecRecord.get_instances():
    print(eq)