import pandas as pd

def from_excel(cls, filename, sheet_name):
    # Read the data from the Excel file
    data = pd.read_excel(filename, sheet_name=sheet_name)
    # Check if the columns in the data match the attributes of the class
    check_class_attrs(cls, set(data.columns))
    # Create a list to store the objects
    objects = []
    # Iterate over the rows in the data
    for index, row in data.iterrows():
        # Create a dictionary of arguments to pass to the class constructor
        args = {}
        for col in data.columns:
            value = row[col]
            prefix = f"_{cls.__name__}__"
            col_noprefix=''
            if col.startswith(prefix):
                col_noprefix = col[len(prefix):]
            else:
                raise ValueError(f"Name of table column {col} do not match attributes of class")
            attr_type = type(getattr(cls, col_noprefix))
            
            if col_noprefix.endswith('_id_list'):
                # Handle Specifications attribute
                specs = list(map(int, value.split(',')))
                args[col_noprefix] = specs
            else:
                args[col_noprefix] = value
        # Create an object from the class using the arguments
        obj = cls(**args)
        # Add the object to the list
        objects.append(obj)
    return objects


def to_excel(cls, objects, filename, sheet_name):
    # Create a list to store the data
    data = []

    # Iterate over the objects
    for obj in objects:
        # Check if the object is an instance of the class
        if not isinstance(obj, cls):
            raise TypeError(f"Object {obj} is not an instance of {cls}")

        # Get the names of the attributes of the object
        object_attrs = set(attr for attr in vars(obj))

        # Check if the attributes of the object match the attributes of the class
        check_class_attrs(cls, object_attrs)

        # Create a dictionary of data from the object
        row = {}
        for attr in object_attrs:
            value = getattr(obj, attr)
            if isinstance(value, list):
                row[attr] = ','.join(str(value[i]) for i in range(len(value)))
            else:
                row[attr] = value

        # Add the dictionary to the list
        data.append(row)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Write the DataFrame to the Excel file
    with pd.ExcelWriter(filename, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)


def check_class_attrs(cls, attrs):
    # Get the names of the attributes of the class
    class_attrs = set()
    for attr in dir(cls):
        if not callable(getattr(cls, attr)) and not attr.startswith("__"):
            class_attrs.add(attr)
            # print(f"Adding attribute {attr} to class_attrs")

    # Print debugging information
    # print(f"class_attrs: {class_attrs}")

    # Remove class name prefix and leading underscores from mangled names in attrs
    prefix = f"_{cls.__name__}__"
    attrs = set(attr[len(prefix):] if attr.startswith(prefix) else attr for attr in attrs)

    # Print debugging information
    # print(f"attrs: {attrs}")

    # Check if the attributes match the attributes of the class
    if attrs != class_attrs:
        print(f"attrs and class_attrs do not match")
        for attr in attrs:
            if attr not in class_attrs:
                print(f"Attribute {attr} is in attrs but not in class_attrs")
        for attr in class_attrs:
            if attr not in attrs:
                print(f"Attribute {attr} is in class_attrs but not in attrs")
        raise ValueError(f"Attributes {attrs} do not match attributes of class {class_attrs}")

