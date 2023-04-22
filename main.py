import os
from acc.model.ins import Instance
from acc.model.sub import *
from acc.model.doc import *
from acc.model.rec import *
from acc.model.nom import *

def initialize_instances():
    '''инициализация тестовыми данными'''
    obj1 = Object(None, 'O1', 'Object1') # type: Object
    prj1 = obj1.Add(Project, None, 'P1', 'Project1') # type: Project
    sl1 = prj1.Add(SpecList, None, 'SL1', 'SpecList1') # type: SpecList
    el1 = prj1.Add(EquipList, None, 'EL1', 'SpecList1') # type: EquipList
    ml1 = prj1.Add(MatList, None, 'ML1', 'MatList1') # type: MatList
    cl1 = prj1.Add(CableList, None, 'CL1', 'CableList1') # type: CableList
    wl1 = prj1.Add(WorkList, None, 'WL1', 'WorkList1') # type: WorkList
    dl1 = prj1.Add(DocList, None, 'DL1', 'DocList1') # type: DocList
    
    return obj1
    
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
        # my_graph = o[0].traverse_graph()
        # my_graph.view()
        
        # read_from_file('data/data.xlsx')
        write_to_file('data/data2.xlsx')

def main():
    app = AccApp()
    app.run()
    
if __name__ == '__main__':
    main()