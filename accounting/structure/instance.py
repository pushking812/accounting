
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

    def add_subinstance(self, instance):
        key = type(instance).__name__
        if key not in self.subinstances:
            self.subinstances[key] = []
        if instance not in self.subinstances[key]:
            self.subinstances[key].append(instance)
            # pass

    def get_subinstance(self, key, index=None):
        if key in self.subinstances:
            value = self.subinstances[key]
            if isinstance(value, list):
                if index is None:
                    raise ValueError("Index hasn't been set")
                return value[index]
            return value
        return []

    def remove_subinstance(self, instance):
        key = type(instance).__name__
        if key in self.subinstances:
            self.subinstances[key].remove(instance)
            Instance.instances_by_class[key].remove(instance)
            instance.CountInstances.remove_instance(instance)

    # @classmethod


    @classmethod
    def display_properties(cls, instance):
        for n in instance.__dict__.items():
            print('----------------------')
            print(n)
        print('========================')

    @classmethod
    def from_excel(cls, file, classes_by_name):
        fromexcel.from_excel(file, classes_by_name)

    @classmethod
    def to_excel(cls, file):
         '''сохраняет свойства и ссылки на дочерние классы в excel'''
         toexcel.to_excel(cls, file)


