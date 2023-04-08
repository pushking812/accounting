from tools.excel import *

class SpecRec:
    def __init__(self, proj_id, spec_id, spec_rec_id, spec_number, value, equip_id):
        self.__proj_id = proj_id
        self.__spec_id = spec_id
        self.__spec_rec_id = spec_rec_id
        self.__spec_number = spec_number
        self.__value = value
        self.__equip_id = equip_id

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename, 'SpecRec')

    @classmethod
    def to_excel(cls, objects, filename):
        to_excel(cls, objects, filename, 'SpecRec')

    def display(self):
        print(f"Project ID: '{self.__proj_id}' Spec ID: '{self.__spec_id}' Spec Rec ID: '{self.__spec_rec_id}' Spec Number: '{self.__spec_number}' Value: '{self.__value}' Equip ID: '{self.__equip_id}'")


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
    def spec_rec_id(self):
        return self.__spec_rec_id

    @spec_rec_id.setter
    def spec_rec_id(self, value):
        self.__spec_rec_id = value

    @property
    def spec_number(self):
        return self.__spec_number

    @spec_number.setter
    def spec_number(self, value):
        self.__spec_number = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def equip_id(self):
        return self.__equip_id

    @equip_id.setter
    def equip_id(self, value):
        self.__equip_id = value