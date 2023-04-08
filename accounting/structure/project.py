from .instance import Instance

class Project(Instance):
    def __init__(self, instance_id = None, project_number = None, project_name = None):
        super().__init__(type(self), instance_id)

        if project_number == None:
            project_number = ''

        if project_name == None:
            project_name = ''

        self.fields['project_number'] = project_number
        self.fields['project_name'] = project_name