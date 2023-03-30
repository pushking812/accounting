from tools.excel import *

class Cat:
    def __init__(self, cat_id, name, desc):
        self.__cat_id = cat_id
        self.__name = name
        self.__desc = desc

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename,'Cat')

    @classmethod
    def to_excel(cls, objects , filename ):
        to_excel(cls, objects , filename ,'Cat')


    def display(self):
        print(f"Cat ID: '{self.__cat_id}' Name: '{self.__name}' Description: '{self.__desc}'")
    
    # Getters / Setters

    @property
    def cat_id(self):
        return self.__cat_id

    @cat_id.setter
    def cat_id(self, value):
        self.__cat_id = value

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