# from . import ins
from ..tools import fromexcel, toexcel
from graphviz import Digraph

class Instance:
    instances_by_class = {}
    count_by_class = {}
    max_id_by_class = {}

    def __init__(self, instance_class, id=None):
        class_name = instance_class.__name__

        instances = Instance.instances_by_class
        self.fields = {}

        if class_name not in instances:
            instances[class_name] = []

        instances[class_name].append(self)

        if id == None:
            id = self.count_instance()

        self.fields['id'] = id

        self.subinstances = {}

    def __del__(self):
        self.uncount_instance()
        
    @classmethod
    def get_instance(cls, id = None, number = None):
        ''' возвращает экземпляр по значению свойства '''
        for instance in cls.instances_by_class:
            # instance.__dict__.items() словарь атрибутов 
            # экземпляра instance в виде пар ключ-значение.
            if isinstance(instance, cls):
                for property_name, property_value in instance.__dict__.items():
                    if property_name == 'id' and property_value == id:
                        return instance
                    elif property_name == 'number' and property_value == number:
                        return instance
                    else:
                        raise ValueError("Wrong property value!")
        return None
        
    @classmethod
    def _get_instance_by_property(cls, id=None, number=None):
        if id is not None:
            return cls.get_instance(id=id)
        elif number is not None:
            return cls.get_instance(number=number)
        else:
            raise ValueError("Property wasn't set!")

    @classmethod
    def update_instance_fields(cls, value, id=None, number=None):
        if value is None:
            raise ValueError("New values weren't set!")
        
        result = cls._get_instance_by_property(id=id, number=number)
        result.fields.update(value)

    @classmethod
    def remove_instance(cls, id=None, number=None):
        result = cls._get_instance_by_property(id=id, number=number)
        
        if result is not None:
            del result
        else:
            raise ValueError("Wrong property!")
        

    def uncount_instance(self):
        ''' уменьшаем индекс экземпляров класса '''
        class_name = self.__class__.__name__
        if class_name in Instance.count_by_class:
            Instance.count_by_class[class_name] -= 1

    def count_instance(self):
        ''' увеличивает индекс экземпляров класса '''
        class_name = self.__class__.__name__
        Instance.count_by_class[class_name] = Instance.count_by_class.get(class_name, 0) + 1
        Instance.max_id_by_class[class_name] = Instance.max_id_by_class.get(class_name, 0) + 1
        return Instance.max_id_by_class[class_name]
    
    def get_number(self):
        ''' возвращает количество количество экземпляров класса'''
        class_name = self.__class__.__name__
        return Instance.count_by_class.get(class_name, 0)
        
    def add_subinstance(self, subinstance):
        ''' добавляет в текущий экземпляр дочерний объект '''
        key = type(subinstance).__name__
        if key not in self.subinstances:
            self.subinstances[key] = []
        if subinstance not in self.subinstances[key]:
            self.subinstances[key].append(subinstance)

    def get_subinstance(self, class_name, id=None):
        ''' по имени класса и номеру объекта получаем дочерний объект 
            если не указан номер, то получаем список всех объектов '''
        if class_name in self.subinstances:
            subinstance = self.subinstances[class_name]
            if isinstance(subinstance, list):
                if id is None:
                    raise ValueError("Index hasn't been set")
                return subinstance[id]
            return subinstance
        return []

    def remove_subinstance(self, class_name, id):
        subinstance = self.get_subinstance(class_name, id)
        if class_name in self.subinstances:
            self.subinstances[class_name].remove(subinstance)
            Instance.instances_by_class[class_name].remove(subinstance)
            Instance.remove_instance(subinstance)

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
    
    
    def traverse_graph(self, depth=None, graph=None):
        if graph is None:
            graph = Digraph()
            graph.node(self.fields['name'], label=f"{self.__class__.__name__}: {self.fields['name']}")
        if depth is None or depth > 0:
            for property_name, property_value in self.__dict__.items():
                if property_name == 'subinstances':
                    for class_name, subinstances in property_value.items():
                        for subinstance in subinstances:
                            graph.edge(self.fields['name'], subinstance.fields['name'])
                            subinstance.traverse_graph(
                                depth=depth-1 if depth is not None else None, graph=graph)
                elif hasattr(property_value, '__dict__'):
                    property_value.traverse_graph(
                        depth=depth-1 if depth is not None else None, graph=graph)
        return graph

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
        for instance in cls.instances_by_class:
            # instance.__dict__.items() словарь атрибутов 
            # экземпляра instance в виде пар ключ-значение.
            for property_name, property_value in instance.__dict__.items():
                if isinstance(instance, cls):
                    result.append((property_name, property_value))
        return result

    
