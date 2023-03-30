from tools.excel import *

class Equip:
    def __init__(self, equip_id, articule, name, cat_id, subcat1_id, subcat2_id):
        self.__equip_id = equip_id
        self.__articule = articule
        self.__name = name
        self.__cat_id = cat_id
        self.__subcat1_id = subcat1_id
        self.__subcat2_id = subcat2_id

    @classmethod
    def from_excel(cls, filename):
        return from_excel(cls, filename, 'Equip')

    @classmethod
    def to_excel(cls, objects, filename):
        to_excel(cls, objects, filename, 'Equip')

    def display(self):
        print(f"Equip ID: '{self.__equip_id}' Articule: '{self.__articule}' Name: '{self.__name}' Cat ID: '{self.__cat_id}' Subcat1 ID: '{self.__subcat1_id}' Subcat2 ID: '{self.__subcat2_id}'")
    
    # Getters / Setters
    @property
    def equip_id(self):
        return self.__equip_id

    @equip_id.setter
    def equip_id(self, value):
        self.__equip_id = value

    @property
    def articule(self):
        return self.__articule

    @articule.setter
    def articule(self, value):
        self.__articule = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

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