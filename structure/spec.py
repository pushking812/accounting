from tools.excel import *

class Spec:
    def __init__(self, proj_id, spec_id, name, desc, file_name, spec_recs_list_id):
        self.__proj_id = proj_id
        self.__spec_id = spec_id
        self.__name = name
        self.__desc = desc
        self.__file_name = file_name
        self.__spec_recs_list_id = spec_recs_list_id

    def add_spec_rec(self, spec_rec):
        self.spec_recs.append(spec_rec)

    def get_spec_recs(self, spec_recs):
        for spec_rec in spec_recs:
            if spec_rec.spec_rec_id == self.__spec_recs_list_id:
                return spec_rec
        return None
        

    def display(self):
        print(f"Project ID: '{self.__proj_id}' Spec ID: '{self.__spec_id}' Name: '{self.__name}' Description: '{self.__desc}' File Name: '{self.__file_name}' Spec Recs List ID: '{self.__spec_recs_list_id}'")

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename, 'Spec')

    @classmethod
    def to_excel(cls, objects, filename):
        to_excel(cls, objects, filename, 'Spec')
    
    # Getters / Setters

    @property
    def proj_id(self):
        return self.__proj_id

    @proj_id.setter
    def proj_id(self, value):
        self.__proj_id = value

    @property
    def spec_id(self):
        return self.__spec_id

    @spec_id.setter
    def spec_id(self, value):
        self.__spec_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def spec_recs_list_id(self):
        return self.__spec_recs_list_id

    @spec_recs_list_id.setter
    def spec_recs_list_id(self, value):
        self.__spec_recs_list_id = value