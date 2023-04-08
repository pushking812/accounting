from tools.excel import *

class Subcat2:
    def __init__(self, cat_id, subcat1_id, subcat2_id, name, desc, ):
        self.__cat_id = cat_id
        self.__subcat1_id = subcat1_id
        self.__subcat2_id = subcat2_id
        self.__name = name
        self.__desc = desc

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename,'Subcat2')

    @classmethod
    def to_excel(cls, objects, filename):
        to_excel(cls, objects, filename,'Subcat2')

    def display(self):
        print(f"Cat ID: '{self.__cat_id}' Subcat1 ID: '{self.__subcat1_id}' Subcat2 ID: '{self.__subcat2_id}' Name: '{self.__name}' Description: '{self.__desc}'")
    
    # Getters / Setters

    @property
    def cat_id(self):
        return self.__cat_id

    @cat_id.setter
    def cat_id(self, value):
        self.__cat_id = value

    @property
    def subcat1_id(self):
        return self.__subcat1_id

    @subcat1_id.setter
    def subcat1_id(self, value):
        self.__subcat1_id = value

    @property
    def subcat2_id(self):
        return self.__subcat2_id

    @subcat2_id.setter
    def subcat2_id(self, value):
        self.__subcat2_id = value

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
