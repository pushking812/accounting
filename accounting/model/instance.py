
from . import countinstances
from ..tools import fromexcel
from ..tools import toexcel


class Instance:
    instances_by_class = {}

    def __init__(self, instance_class, instance_id=None):
        class_name = instance_class.__name__

        instances = Instance.instances_by_class
        self.fields = {}

        if class_name not in instances:
            instances[class_name] = []

        instances[class_name].append(self)

        if instance_id == None:
            instance_id = countinstances.CountInstances.add_instance(self)

        self.fields = {
            'id_by_class': instance_id
        }

        self.subinstances = {}


    def add_subinstance(self, subinstance):
        ''' добавляет в текущий экземпляр дочерний объект '''
        key = type(subinstance).__name__
        if key not in self.subinstances:
            self.subinstances[key] = []
        if subinstance not in self.subinstances[key]:
            self.subinstances[key].append(subinstance)


    def get_subinstance(self, class_name, id_by_class=None):
        ''' по имени класса и номеру объекта получаем дочерний объект 
            если не указан номер, то получаем список всех объектов '''
        if class_name in self.subinstances:
            subinstance = self.subinstances[class_name]
            if isinstance(subinstance, list):
                if id_by_class is None:
                    raise ValueError("Index hasn't been set")
                return subinstance[id_by_class]
            return subinstance
        return []


    def remove_subinstance(self, instance):
        key = type(instance).__name__
        if key in self.subinstances:
            self.subinstances[key].remove(instance)
            Instance.instances_by_class[key].remove(instance)
            instance.CountInstances.remove_instance(instance)

    def traverse_properties(self, depth=None):
        print(f"---------------------------")
        print(f"Instance '{self.fields['name']}' of class {self.__class__.__name__}:")
        if depth is None or depth > 0:
            for property_name, property_value in self.__dict__.items():
                if property_name == 'subinstances':
                    for class_name, subinstances in property_value.items():
                        print(f"{class_name} (list of {class_name})")
                        for subinstance in subinstances:
                            subinstance.traverse_properties(
                                depth=depth-1 if depth is not None else None)
                else:
                    print(property_name, property_value)
                    if hasattr(property_value, '__dict__'):
                        property_value.traverse_properties(
                            depth=depth-1 if depth is not None else None)


    @classmethod
    def display_properties(cls, instance):
        for n in instance.__dict__.items():
            print('----------------------')
            print(n)
        print('========================')


    @classmethod
    def from_excel(cls, file, classes_by_name):
        ''' загружает данные из excel в экземпляры классов'''
        fromexcel.from_excel(file, classes_by_name)


    @classmethod
    def to_excel(cls, file):
         '''сохраняет данные экземпляров классов в excel'''
         toexcel.to_excel(cls, file)


    @classmethod
    def add_field(cls, value, key):
        ''' добавляет простое поле данных в экземпляр класса '''
        for instance in cls.instances_by_class:
            if isinstance(instance, cls):
                instance.fields[key] = value

    @classmethod
    def get_field_values(cls, key):
        ''' получает значения указанного поля данных для всех экземпляров класса '''
        result=[]
        result.append(key)
        for instance in cls.instances_by_class:
            if isinstance(instance, cls):
                 if key in instance.fields:
                    result.append(instance.fields[key])
        return result


    @classmethod
    def get_instances(cls):
        ''' возвращает список кортежей (имя свойства, значение) для экземпляров класса'''
        result=[]
        for instance in cls.instances:
            # instance.__dict__.items() словарь атрибутов 
            # экземпляра instance в виде пар ключ-значение.
            for property_name, property_value in instance.__dict__.items():
                if isinstance(instance, cls):
                    result.append((property_name, property_value))
        return result
    
