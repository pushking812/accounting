import os
from accounting.model.instance import Instance
from accounting.model.subject import *
from accounting.model.doc import *
from accounting.model.docrecord import *
from accounting.model.nomenclature import *

def initialize_instances():
    '''инициализация тестовыми данными'''
    
    # справочник объектов
    objs = [Object(**d) for d in 
        [
            {'id': None, 'number': f'O{i}', 'name': f'Object1 O{i}'}
            for i in range(1)
        ] 
    ]

    # справочник проектов
    projs = [Project(**d) for d in 
        [
            {'id': None, 'number': f'P{i}', 'name': f'Project P{i}'}
            for i in range(3)
        ] 
    ]
    
    # справочник спецификаций
    specs = [SpecLst(**d) for d in
        [ 
            {'id': None, 'number': f'SL{i}', 'name': f'SpecLst P{i}'}
            for i in range(6)
        ] 
    ]
    
    # справочник кабельных журналов
    cabjs = [CableLst(**d) for d in
        [ 
            {'id': None, 'number': f'CL{i}', 'name': f'CableLst P{i}'}
            for i in range(3)
        ] 
    ]
    
    # справочник кабельных журналов
    wrkls = [WorkLst(**d) for d in
        [ 
            {'id': None, 'number': f'WL{i}', 'name': f'WorkLst P{i}'}
            for i in range(3)
        ] 
    ]

    # справочник ведомостей работ
    wrks = [Work(**d) for d in
        [ 
            {'id': None, 'number': f'S{i}', 'name': f'Work P{i}'}
            for i in range(6)
        ] 
    ]
    
    # справочник категорий материалов и оборудования
    cats = [Cat(**d) for d in
        [
           {'id': None, 'number': f'C{i}' , 'name': f'Cat C{i}'}
           for i in range(24)
        ] 
    ]
    
    # справочник материалов и оборудования
    equips = [Equipment(**d) for d in
        [
           {'id': None, 'number': f'E{i}', 'name':  f'Equipment E{i}'}
           for i in range(24)
        ] 

    ]
    
    # дерево категорий материалов и оборудования
    cat_recs=[]
    for i in range(1, 14, 4):
        cat_recs.append(CatRecord(**{'id': i  , 'name':f'CatRecord{i}'  , 'subinstances': [cats[i-1]]}))                   # 0.0.0
        cat_recs.append(CatRecord(**{'id': i+1, 'name':f'CatRecord{i+1}', 'subinstances': [cats[i]]}))                 # 0.0.1
        cat_recs.append(CatRecord(**{'id': i+2, 'name':f'CatRecord{i+2}', 'subinstances': [cats[i+1], cat_recs[-1], cat_recs[-2]]})) # 0.0
        cat_recs.append(CatRecord(**{'id': i+3, 'name':f'CatRecord{i+3}', 'subinstances': [cats[i+2], cat_recs[-1]]}))         # 0


    # список записей с информацией о материалах и оборудовании
    # (категория материала, документы качества на материал и т.п.)
    equip_recs = [EquipRecord(**d) for d in 
        [
            {'id': None, 'name':f'EquipRecord{i}',
             'subinstances': [equips[i],  cat_recs[i]]}
            for i in range(16)
        ]
    ]

    # список кабельных журналов со связанной номенклатурой
    cabj_recs = [CableJnlRecord(**d) for d in 
        [
            {'id': None, 'name':f'CableJnlRecord{j}',
             'subinstances': [cabjs[i//9]]+[equip_recs[i//2] for i in range(j,j+3)]}
            for j in range(0, 25, 9)
        ]
    ]
    
    # список ведомостей работ
    wrkl_recs = [WorkLstRecord(**d) for d in 
        [
            {'id': None, 'name':f'WorkLstRecord{j}',
             'subinstances': [wrkls[i//9]]+[wrks[i//5] for i in range(j,j+3)]}
            for j in range(0, 25, 9)
        ]
    ]
    
    # список спецификаций со связанной номенклатурой
    spec_recs = [SpecRecord(**d) for d in 
        [
            {'id': None, 'name':f'SpecRecord{j}', 
             'subinstances': [specs[j//2]]+[equip_recs[i] for i in range(j,j+2)]}
            for j in range(0, 12, 2)
        ]
    ]

    # список проектов со связанными спецификациями
    proj_recs = [ProjectRecord(**d) for d in 
        [
            {'id': None, 'name':f'ProjectRecord{i}',
             'subinstances': [projs[i]]+[wrkl_recs[i]]+[cabj_recs[i]]+[spec_recs[i]]
            }
            for i in range(3)
        ]
    ]
    
    # список объектов со связанными проектами
    obj_recs = [ObjectRecord(**d) for d in 
        [
            {'id': None, 'name':f'ObjectRecord{j}',
             'subinstances': [objs[j]]+[proj_recs[i] for i in range(j,j+3)]}
            for j in range(1)
        ]
    ]
    
    return obj_recs
    
# получаем словарь хранящий существующие типы классов по их названиям 
classes_by_name = {name: obj for name, obj in globals().items() if isinstance(obj, type)}
pass

def read_from_file(file):
    '''считывает данные в экземпляры классов из существующего файла'''
    Instance.from_excel(file, classes_by_name)

def write_to_file(file):
    '''записывает данные экземпляров классов в существующий файл'''
    Instance.to_excel(file)

o=[]

class AccApp:
    def __init__(self):
        global o
        o=initialize_instances()
        pass

    def run(self):
        my_graph = o[0].traverse_graph()
        my_graph.view()
        
        # read_from_file('data/data.xlsx')
        write_to_file('data/data2.xlsx')

def main():
    app = AccApp()
    app.run()


if __name__ == '__main__':
    main()








    
