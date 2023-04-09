import os
from accounting.model.project import Project
from accounting.model.object import Object
from accounting.model.record import ObjectRecord, ProjectRecord, SpecRecord, EquipRecord, CatRecord
from accounting.model.instance import Instance
from accounting.model.specification import Spec
from accounting.model.equipment import Equip
from accounting.model.category import Cat

def initialize_instances():
    '''инициализация тестовыми данными'''
    
    # справочник объектов
    objects = [Object(**d) for d in 
        [
            {'instance_id': None, 'object_number': f'O{i}', 'object_name': f'Object1 O{i}'}
            for i in range(1)
        ] 
    ]

    # справочник проектов
    projects = [Project(**d) for d in 
        [
            {'instance_id': None, 'project_number': f'P{i}', 'project_name': f'Project P{i}'}
            for i in range(3)
        ] 
    ]
    
    # справочник спецификаций
    specs = [Spec(**d) for d in
        [ 
            {'instance_id': None, 'spec_number': f'S{i}', 'spec_name': f'Spec P{i}'}
            for i in range(6)
        ] 
    ]

    # справочник категорий материалов и оборудования
    cat = [Cat(**d) for d in
        [
           {'instance_id': None, 'cat_number': f'C{i}' , 'cat_name': f'Cat C{i}'}
           for i in range(24)
        ] 
    ]
    
    # справочник материалов и оборудования
    equipments = [Equip(**d) for d in
        [
           {'instance_id': None, 'equip_number': f'E{i}', 'equip_name':  f'Equip E{i}'}
           for i in range(24)
        ] 
    ]
    
    cr=[]
    for i in range(1, 14, 4):
            cr.append({'instance_id': i, 'subinstances':  [cat[i]]})    # 0
            cr.append({'instance_id': i+1, 'subinstances': [cat[i+1], cat[i+2]]}) # 0.0
            cr.append({'instance_id': i+2, 'subinstances': None})                 # 0.0.0
            cr.append({'instance_id': i+3, 'subinstances': None})                 # 0.0.1
        
    # дерево категорий материалов и оборудования
    cats_records = [CatRecord(**d) for d in cr]


    # список записей с информацией о материалах и оборудовании
    # (категория материала, документы качества на материал и т.п.)
    equips_records = [EquipRecord(**d) for d in 
        [
            {'instance_id': None, 'subinstances': [equipments[i],  cats_records[i]]}
            for i in range(16)
        ]
    ]

    # список записей с информацией об оборудовании для каждой спецификации
    # записи для документа Спецификация 
    specs_records = [SpecRecord(**d) for d in 
        [
            {'instance_id': None, 'subinstances': [specs[0]]+[equips_records[i] for i in range(0,2)]},
            {'instance_id': None, 'subinstances': [specs[1]]+[equips_records[i] for i in range(2,4)]},
            {'instance_id': None, 'subinstances': [specs[2]]+[equips_records[i] for i in range(4,6)]},
            {'instance_id': None, 'subinstances': [specs[3]]+[equips_records[i] for i in range(6,8)]},
            {'instance_id': None, 'subinstances': [specs[4]]+[equips_records[i] for i in range(8,10)]},
            {'instance_id': None, 'subinstances': [specs[5]]+[equips_records[i] for i in range(10,12)]}
        ]
    ]

    # список проектов со связанными спецификациями
    projects_records = [ProjectRecord(**d) for d in 
        [
            {'instance_id': None, 'subinstances': [projects[0]]+[equips_records[i] for i in range(0,2)]},
            {'instance_id': None, 'subinstances': [projects[1]]+[equips_records[i] for i in range(2,4)]},
            {'instance_id': None, 'subinstances': [projects[2]]+[equips_records[i] for i in range(4,6)]}
        ]
    ]
    
    # список объектов, корневая сущность 
    objects_records = [ObjectRecord(**d) for d in 
        [
            {'instance_id': None, 'subinstances': [objects[0], s]}
            for s in projects_records
        ]
    ]
    
    
### получаем словарь хранящий существующие типы классов по их названиям 
classes_by_name = {name: obj for name, obj in globals().items() if isinstance(obj, type)}
pass

def read_from_file(file):
    '''считывает данные в экземпляры классов из существующего файла'''
    Instance.from_excel(file, classes_by_name)

def write_to_file(file):
    '''записывает данные экземпляров классов в существующий файл'''
    Instance.to_excel(file)


class AccApp:
    def __init__(self):
        # initialize_instances()
        pass

    def run(self):
        read_from_file('data/data.xlsx')
        write_to_file('data/data2.xlsx')

def main():
    app = AccApp()
    app.run()


if __name__ == '__main__':
    main()








    
