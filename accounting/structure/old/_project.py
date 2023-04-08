from tools.excel import *

class Project:
    def __init__(self, proj_id, number, name, desc, specs_id_list):
        self.__proj_id = proj_id
        self.__number = number
        self.__name = name
        self.__desc = desc
        self.__specs_id_list = specs_id_list

    def add_spec(self, spec):
        self.specs.append(spec)

    def get_specs(self, specs):
        result = []
        for spec in specs:
            if spec.spec_id in self.__specs_id_list:
                result.append(spec)
        return result

    def display(self):
        print(f"Project ID: '{self.__proj_id}' Number: '{self.__number}' Name: '{self.__name}' Description: '{self.__desc}' Specifications: '{self.__specs_id_list}'")

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename, 'Project')

    @classmethod
    def to_excel(cls, objects, filename):
        to_excel(cls, objects, filename, 'Project')
    
    # Getters / Setters

    @property
    def proj_id(self):
        return self.__proj_id

    @proj_id.setter
    def proj_id(self, value):
        self.__proj_id = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

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
    def specs_id_list(self):
        return self.__specs_id_list

    @specs_id_list.setter
    def specs_id_list(self, value):
        self.__specs_id_list = value