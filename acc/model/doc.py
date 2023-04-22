from .ins import Instance
from .rec import *

class Doc(Instance):
    def __init__(self, instance_class, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(instance_class, id)

        for e in [doc_number, doc_name, sheet_count, doc_revision, doc_date]:
            e = '' if e == None else None

        self.fields['doc_number'] = doc_number
        self.fields['doc_name'] = doc_name
        self.fields['doc_date'] = doc_date
        self.fields['doc_revision'] = doc_revision
        self.fields['sheet_count'] = sheet_count
        
        self.isDocSubinstance(instance_class)
        if doctype_instance != None:
            if isinstance(doctype_instance, DocType):
                self.add_subinstance(doctype_instance)
            else:
                raise ValueError('Instance isn\'t DocType type!')

    def Add(self, class_type, id = None, number = None, name = None):
        ''' class_type SpecList: SpecRecord, class_type EquipList: EquipRecord, 
        class_type MatList: MatRecord, class_type CableList: CableRecord '''
        
        instance = class_type(id, number, name)
        
        if self.isDocSubinstance(class_type):
            self.add_subinstance(instance)
            return instance
        else:
           raise ValueError('Wrong instance class!')
        
    def Get(self, class_type, id = None):
        ''' class_type SpecList: SpecRecord, class_type EquipList: EquipRecord, 
        class_type MatList: MatRecord, class_type CableList: CableRecord '''
        
        if self.isDocSubinstance(class_type):
            return self.get_subinstance(class_type, id)
        else:
           raise ValueError('Wrong instance class!')
       
    def Remove(self, instance_class, id = None):
        ''' class_type SpecList: SpecRecord, class_type EquipList: EquipRecord, 
        class_type MatList: MatRecord, class_type CableList: CableRecord '''
        
        if self.isDocSubinstance(instance_class):
            self.remove_subinstance(instance_class, id)
        else:
           raise ValueError('Wrong instance class!') 
        
    def isDocSubinstance(self, instance_class):
        self_class = type(self)
        
        ok = False
        if self_class == SpecList and instance_class in [SpecRecord, EquipRecord, CableRecord]:
            ok = True
        elif self_class == EquipList and instance_class in [EquipRecord]:
            ok = True
        elif self_class == MatList and instance_class in [MatRecord]:
            ok = True
        elif self_class == CableList and instance_class in [CableRecord]:
            ok = True
        elif instance_class in [DocType]:
            ok = True
            
        return ok
        
class SpecList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, 
                         doc_revision, sheet_count)
        
        self.add_subinstance(DocType(doctype_number='1.1', doctype_name='Specification'))
        
        # self.add_subinstance(EquipRecord())
        # self.add_subinstance(CableRecord())
        # self.add_subinstance(MatRecord())

class EquipList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, 
                         doc_revision, sheet_count, doctype_instance)

        # self.add_subinstance(EquipRecord())

class MatList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, doc_revision, 
                         sheet_count, doctype_instance)
        
        # self.add_subinstance(MatRecord())

class CableList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, doc_revision, 
                         sheet_count, doctype_instance)

        # self.add_subinstance(CableRecord())

class WorkList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, doc_revision, 
                         sheet_count, doctype_instance)

        # self.add_subinstance(WorkRecord())

class DocList(Doc):
    def __init__(self, id = None, doc_number = None, doc_name = None,
                 doc_date = None, doc_revision = None, sheet_count = None,
                 doctype_instance = None):
        super().__init__(type(self), id, doc_number, doc_name, doc_date, doc_revision, 
                         sheet_count, doctype_instance)
        
        # self.add_subinstance(DocRecord())

class DocType(Instance):
    def __init__(self, id = None, doctype_number = None, doctype_name = None):
        super().__init__(type(self), id)

        for e in [doctype_number, doctype_name]:
            e = '' if e == None else None

        self.fields['doc_number'] = doctype_number
        self.fields['doctype_name'] = doctype_name
        
#         if doctypetype_instance != None:
#             if isinstance(doctypetype_instance, DocTypeType):
#                 self.add_subinstance(doctypetype_instance)
#             else:
#                 raise ValueError('Instance isn\'t DocTypeType type!')

# class DocTypeType(Instance):
#     def __init__(self, typetype = None):
#         super().__init__(type(self))

#         if typetype == None:
#             typetype = 'not set'
        
#         self.fields['typetype'] = typetype