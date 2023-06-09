

# specs_data = [
#     {'id': None, 'number': 'S1', 'name': 'Spec1'},
#     {'id': None, 'number': 'S2', 'name': 'Spec2'},
#     {'id': None, 'number': 'S3', 'name': 'Spec3'},
#     {'id': None, 'number': 'S4', 'name': 'Spec4'},
#     {'id': None, 'number': 'S5', 'name': 'Spec5'},
#     {'id': None, 'number': 'S6', 'name': 'Spec6'},
# ]
# spec_recs_data = [
#     {'id': None, 'number': 'S1', 'name': 'Spec1'},
#     {'proj_id': 0, 'spec_id': 0, 'spec_rec_id': 0,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 0, 'spec_id': 0, 'spec_rec_id': 0,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
#     {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1,
#         'number': 1, 'value': 100.0, 'equip_id': 0},
#     {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 0, 'spec_id': 1, 'spec_rec_id': 1,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
#     {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2,
#         'number': 1, 'value': 100.0, 'equip_id': 0},
#     {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 1, 'spec_id': 2, 'spec_rec_id': 2,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
#     {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3,
#         'number': 1, 'value': 100.0, 'equip_id': 0},
#     {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 1, 'spec_id': 3, 'spec_rec_id': 3,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
#     {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4,
#         'number': 1, 'value': 100.0, 'equip_id': 0},
#     {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 2, 'spec_id': 4, 'spec_rec_id': 4,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
#     {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5,
#         'number': 1, 'value': 100.0, 'equip_id': 0},
#     {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5,
#         'number': 2, 'value': 200.0, 'equip_id': 1},
#     {'proj_id': 2, 'spec_id': 5, 'spec_rec_id': 5,
#         'number': 3, 'value': 300.0, 'equip_id': 2},
# ]
# equips_data = [
#     {'equip_id': 0, 'articule': 'Equip_articule1', 'name': 'Equip_name1',
#         'cat_id': 0, 'subcat1_id': 0, 'subcat2_id': 0},
#     {'equip_id': 1, 'articule': 'Equip_articule2', 'name': 'Equip_name2',
#         'cat_id': 1, 'subcat1_id': 0, 'subcat2_id': 0},
#     {'equip_id': 2, 'articule': 'Equip_articule3', 'name': 'Equip_name3',
#         'cat_id': 2, 'subcat1_id': 0, 'subcat2_id': 0}
# ]
# cats_data = [
#     {'cat_id': 0, 'name': 'Cat1', 'desc': 'Cat1_desc'},
#     {'cat_id': 0, 'name': 'Cat1', 'desc': 'Cat1_desc'},
#     {'cat_id': 0, 'name': 'Cat1', 'desc': 'Cat1_desc'}
# ]
# subcats1_data = [
#     {'cat_id': 0, 'subcat1_id': 0, 'name': 'Subcat11', 'desc': 'Subcat11_desc'},
#     {'cat_id': 1, 'subcat1_id': 0, 'name': 'Subcat21', 'desc': 'Subcat21_desc'},
#     {'cat_id': 2, 'subcat1_id': 0, 'name': 'Subcat31', 'desc': 'Subcat31_desc'}
# ]
# subcats2_data = [
#     {'cat_id': 0, 'subcat1_id': 0, 'subcat2_id': 0,
#         'name': 'Subcat111', 'desc': 'Subcat111_desc'},
#     {'cat_id': 1, 'subcat1_id': 0, 'subcat2_id': 0,
#         'name': 'Subcat211', 'desc': 'Subcat211_desc'},
#     {'cat_id': 2, 'subcat1_id': 0, 'subcat2_id': 0,
#         'name': 'Subcat311', 'desc': 'Subcat311_desc'}
# ]
# self.projects = []
# for pd in projects_data:
#     self.projects.append(Project(**pd))
# for p in self.projects:
#     print("---------------")
#     p.display()
# self.specs = []
# for sd in specs_data:
#     self.specs.append(SpecLst(**sd))
# for po in self.projects:
#     for so in self.specs:
#         if po.proj_id == so.proj_id:
#             po.add_spec(so)
# self.spec_recs = []
# for rd in spec_recs_data:
#     self.spec_recs.append(SpecRec(**rd))
# for so in self.specs:
#     for sro in self.spec_recs:
#         if so.spec_id == sro.spec_id:
#             so.add_spec_rec(sro)
# self.equips = []
# for ed in equips_data:
#     self.equips.append(Nomenclature(**ed))
# self.cats = []
# for cd in cats_data:
#     self.cats.append(Cat(**cd))
# self.subcats1 = []
# for cd in subcats1_data:
#     self.subcats1.append(Subcat1(**cd))
# self.subcats2 = []
# for cd in subcats2_data:
#     self.subcats2.append(Subcat2(**cd))