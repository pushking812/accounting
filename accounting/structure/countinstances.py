class CountInstances:
    count_by_class = {}
    max_id_by_class = {}

    @classmethod
    def add_instance(cls, instance):
        class_name = instance.__class__.__name__
        cls.count_by_class[class_name] = cls.count_by_class.get(class_name, 0) + 1
        cls.max_id_by_class[class_name] = cls.max_id_by_class.get(class_name, 0) + 1
        return cls.max_id_by_class[class_name]
    
    @classmethod
    def remove_instance(cls, instance):
        class_name = instance.__class__.__name__
        if class_name in cls.count_by_class:
            cls.count_by_class[class_name] -= 1
        
    @classmethod
    def get_number(cls, instance):
        class_name = instance.__class__.__name__
        return cls.count_by_class.get(class_name, 0)
    
