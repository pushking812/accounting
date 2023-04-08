from openpyxl import Workbook

def to_excel(cls, filename):
    '''сохраняет свойства и ссылки на дочерние классы в excel'''
    # создаем книгу
    wb = Workbook()
    # удаляем лист создаваемый по умолчанию
    wb.remove(wb['Sheet'])

    # проходим по всем классам (ключам) instances_by_class,
    # для заполнения листов (классы) данными (экземпляры)
    # instances = {'ClassName1':[<class ClassName1 object at ...>, ...]}
    for class_name, instances in cls.instances_by_class.items():
        # по имени класса создаем лист в книге
        ws = wb.create_sheet(class_name)
        # получаем заголовки столбцов листа класса
        headers = get_headers(instances)
        # добавляем строку с заголовками столбцов на лист класса
        ws.append(headers)
        # проходим по всем сущностям класса для заполнения строк данными
        for instance in instances:
            # получаем строку
            row = get_row(instance, headers)
            # добавляем строку на лист
            ws.append(row)
    # записываем книгу в файл
    wb.save(filename)

def get_headers(instances):
    '''получает заголовки столбцов по названием свойств и экземпляров дочерних классов'''
    # создаем множество для избежания дублирования заголовков столбцов
    headers = set()
    # проходимся по всем экземплярам класса
    for instance in instances:
        # используем ключи из словаря field в качестве заголовков столбцов
        # по идее набор ключей у всех экземпляров должен быть одинаковым
        headers.update(instance.fields.keys())

        # добавляем ключи из словаря subinstances в качестве заголовков столбцов
        for subinstance_name in instance.subinstances.keys():
            # добавляем в конец заголовков постфикс _instances, чтобы при загрузке  
            # из эксель можно было их (столбцы со ссылками на экземпляры) отличить 
            # от столбцов с названиями из fields (простыми данными)
            headers.add(f"{subinstance_name}_instance")
    return list(headers)


def get_row(instance, headers):
    '''получает строку данных для экземпляра класса'''
    row = []
    # проходим по всем существующим заголовкам данного класса
    for header in headers:
        # если заголовок заканчивается _instance, то это экземпляр класса
        if header.endswith("_instance"):
            # убираем постфикс из названия класса экземпляра
            subinstances_class_name = header[:-len("_instance")]
            # получаем экземпляры этого класса из subinstances, если такого ключа нет
            # то пустой список
            subinstances = instance.subinstances.get(subinstances_class_name, [])
            # через запятую перечисляем номера id_by_class экземпляров, 
            # если их несколько и добавляем их в поле строки данных
            row.append(",".join(str(subinstance.fields["id_by_class"]) 
                                for subinstance in subinstances))
        # если этот заголовок из field (простые данные) добавляем данные в строку
        else:
            row.append(instance.fields.get(header))
    return row
