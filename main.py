import os
from accounting.structure.project import Project
from accounting.structure.object import Object
from accounting.structure.record import ObjectRecord, ProjectRecord
from accounting.structure.instance import Instance

def initialize_instances():
    '''инициализация тестовыми данными'''
    # справочник объектов, содержит данные о существующих объектах
    objects = [Object(**od) for od in 
        [
            {'instance_id': None, 'object_number': 'O1', 'object_name': 'Object1'}
        ]
    ]

    # справочник проектов, содержит данные о существующих объектах
    projects = [Project(**pd) for pd in 
        [
            {'instance_id': None, 'project_number': 'P1', 'project_name': 'Project1'},
            {'instance_id': None, 'project_number': 'P2', 'project_name': 'Project2'},
            {'instance_id': None, 'project_number': 'P3', 'project_name': 'Project3'}
        ]
    ]

    # список проектов, проекты дочки объектов 
    projects_records = [ProjectRecord(**prd) for prd in 
        [
            {'instance_id': None, 'subinstances': [p]}
            for p in projects
        ]
    ]

    # список объектов, корневая сущность 
    objects_records = [ObjectRecord(**ord) for ord in 
        [
            {'instance_id': None, 'subinstances': [objects[0], pr]}
            for pr in projects_records
        ]
    ]
    pass

### получаем словарь хранящий существующие типы классов по их названиям 
classes_by_name = {name: obj for name, obj in globals().items() if isinstance(obj, type)}
pass

def read_from_file(file):
    '''считывает данные из существующего файла'''
    Instance.from_excel(file, classes_by_name)

def write_to_file(file):
    '''записывает данные экземпляров классов в существующий файл'''
    Object.to_excel(file)
    Project.to_excel(file)
    ObjectRecord.to_excel(file)
    ProjectRecord.to_excel(file)


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








    
