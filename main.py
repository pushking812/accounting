from structure.project import *
from structure.spec import *
from structure.spec_rec import *
from structure.equip import *
from structure.cat import *
from structure.subcat1 import *
from structure.subcat2 import *

class AccApp:
    def __init__(self):

        projects_data = [
            {'proj_id': 0, 'number': 'P1', 'name': 'Project1', 'desc': 'Project1_desc', 'specs_id_list': [0,1]},
            {'proj_id': 1, 'number': 'P2', 'name': 'Project2', 'desc': 'Project2_desc', 'specs_id_list': [2,3]},
            {'proj_id': 2, 'number': 'P3', 'name': 'Project3', 'desc': 'Project3_desc', 'specs_id_list': [4,5]}
        ]

        self.projects=[]
        for pd in projects_data:
            self.projects.append(Project(**pd))

        # for p in self.projects:
        #     print("---------------")
        #     p.display()

        specs_data = [
            {'proj_id': 0, 'spec_id': 0, 'name': 'Spec1', 'desc': 'Spec1_desc', 'file_name': 'specfile1.xlsx','spec_recs_list_id':0},
            {'proj_id': 0, 'spec_id': 1, 'name': 'Spec2', 'desc': 'Spec2_desc', 'file_name': 'specfile2.xlsx','spec_recs_list_id':1},
            {'proj_id': 1, 'spec_id': 2, 'name': 'Spec3', 'desc': 'Spec3_desc', 'file_name': 'specfile3.xlsx','spec_recs_list_id':2},
            {'proj_id': 1, 'spec_id': 3, 'name': 'Spec4', 'desc': 'Spec4_desc', 'file_name': 'specfile4.xlsx','spec_recs_list_id':3},
            {'proj_id': 2, 'spec_id': 4, 'name': 'Spec5', 'desc': 'Spec5_desc', 'file_name': 'specfile5.xlsx','spec_recs_list_id':4},
            {'proj_id': 2, 'spec_id': 5, 'name': 'Spec6', 'desc': 'Spec6_desc', 'file_name': 'specfile6.xlsx','spec_recs_list_id':5}
        ]

        self.specs=[]
        for sd in specs_data:
            self.specs.append(Spec(**sd))

        # for po in self.projects:
        #     for so in self.specs:
        #         if po.proj_id == so.proj_id:
        #             po.add_spec(so)

        spec_recs_data = [
            {'proj_id': 0, 'spec_id': 0, 'spec_rec_id': 0, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 0, 'spec_id': 0, 'spec_rec_id': 0, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 0, 'spec_id': 0, 'spec_rec_id': 0, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
            {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
            {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
            {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
            {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
            {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5, 'spec_number': 1, 'value': 100.0, 'equip_id':0},
            {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5, 'spec_number': 2, 'value': 200.0, 'equip_id':1},
            {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5, 'spec_number': 3, 'value': 300.0, 'equip_id':2},
        ]

        self.spec_recs=[]
        for rd in spec_recs_data:
            self.spec_recs.append(SpecRec(**rd))

        # for so in self.specs:
        #     for sro in self.spec_recs:
        #         if so.spec_id == sro.spec_id:
        #             so.add_spec_rec(sro)

        equips_data = [
            {'equip_id':0, 'articule':'Equip_articule1', 'name':'Equip_name1', 'cat_id':0, 'subcat1_id':0, 'subcat2_id':0},
            {'equip_id':1, 'articule':'Equip_articule2', 'name':'Equip_name2', 'cat_id':1, 'subcat1_id':0, 'subcat2_id':0},
            {'equip_id':2, 'articule':'Equip_articule3', 'name':'Equip_name3', 'cat_id':2, 'subcat1_id':0, 'subcat2_id':0}
        ]

        self.equips=[]
        for ed in equips_data:
            self.equips.append(Equip(**ed))

        cats_data = [
            {'cat_id':0, 'name':'Cat1', 'desc':'Cat1_desc'},
            {'cat_id':0, 'name':'Cat1', 'desc':'Cat1_desc'},
            {'cat_id':0, 'name':'Cat1', 'desc':'Cat1_desc'}
        ]

        self.cats=[]
        for cd in cats_data:
            self.cats.append(Cat(**cd))

        subcats1_data = [
            {'cat_id':0, 'subcat1_id':0, 'name':'Subcat11', 'desc':'Subcat11_desc'},
            {'cat_id':1, 'subcat1_id':0, 'name':'Subcat21', 'desc':'Subcat21_desc'},
            {'cat_id':2, 'subcat1_id':0, 'name':'Subcat31', 'desc':'Subcat31_desc'}
        ]

        self.subcats1=[]
        for cd in subcats1_data:
            self.subcats1.append(Subcat1(**cd))

        subcats2_data = [
            {'cat_id':0, 'subcat1_id':0, 'subcat2_id':0, 'name':'Subcat111', 'desc':'Subcat111_desc'},
            {'cat_id':1, 'subcat1_id':0, 'subcat2_id':0, 'name':'Subcat211', 'desc':'Subcat211_desc'},
            {'cat_id':2, 'subcat1_id':0, 'subcat2_id':0, 'name':'Subcat311', 'desc':'Subcat311_desc'}
        ]

        self.subcats2=[]
        for cd in subcats2_data:
            self.subcats2.append(Subcat2(**cd))

    def test_from_excel(self):
       self.projects=Project.from_excel('data.xlsx')
       self.specs=Spec.from_excel('data.xlsx')
       self.spec_recs=SpecRec.from_excel('data.xlsx')
       self.equips=Equip.from_excel('data.xlsx')
       self.cats=Cat.from_excel('data.xlsx')
       self.subcats1=Subcat1.from_excel('data.xlsx')
       self.subcats2=Subcat2.from_excel('data.xlsx')

       self.projects[0].get_specs(self.specs)[0].get_spec_recs(self.spec_recs).display()

    #    for i in range(len(self.projects)):
    #         print("=======================================")
    #         for p in self.projects[i].get_specs(self.specs):
    #             print("---------------")
    #             p.display()

        # for p in projects:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in specs:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in spec_recs:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in equips:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in cats:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in subcats1:
        #     print("---------------")
        #     p.display()

        # print("=======================================")
        # for p in subcats2:
        #     print("---------------")
        #     p.display()

    def test_to_excel(self):
        Project.to_excel(self.projects, 'data.xlsx')
        Spec.to_excel(self.specs, 'data.xlsx')
        SpecRec.to_excel(self.spec_recs, 'data.xlsx')
        Equip.to_excel(self.equips, 'data.xlsx')
        Cat.to_excel(self.cats, 'data.xlsx')
        Subcat1.to_excel(self.subcats1, 'data.xlsx')
        Subcat2.to_excel(self.subcats2, 'data.xlsx')




    def run(self):
        # self.test_to_excel()
        self.test_from_excel()

def main():
    app = AccApp()
    app.run()


if __name__ == '__main__':
    main()
