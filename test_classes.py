class Document:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_children(self, children):
        for child in children:
            self.children.append(child)
    
    def read(self):
        return self.name
    
    def write(self, name):
        self.name = name

class TextDocument(Document):
    def __init__(self, name):
        super().__init__(name)
        
    
class SpreadsheetDocument(Document):
    def __init__(self, name):
        super().__init__(name)
 

class PresentationDocument(Document):
    def __init__(self, name):
        super().__init__(name)

class MyApp:
    def __init__(self):
        self.root_doc = Document('Root')
        self.text_doc1 = TextDocument('Level 1 left')
        self.text_doc2 = TextDocument('Level 1 right')
        self.spreadsheet_doc1 = SpreadsheetDocument('Level 2 left')
        self.spreadsheet_doc2 = SpreadsheetDocument('Level 2 right')
        self.presentation_doc1 = PresentationDocument('Level 3 left 1')
        self.presentation_doc2 = PresentationDocument('Level 3 left 2')
        self.presentation_doc3 = PresentationDocument('Level 3 right 1')
        self.presentation_doc4 = PresentationDocument('Level 3 right 2')

        self.root_doc.add_children([self.text_doc1, self.text_doc2])
        self.text_doc1.add_children([self.spreadsheet_doc1])
        self.text_doc2.add_children([self.spreadsheet_doc2])
        self.spreadsheet_doc1.add_children([self.presentation_doc1, self.presentation_doc2])
        self.spreadsheet_doc2.add_children([self.presentation_doc3, self.presentation_doc4])

        self.doc_dict = {
            "text": [self.text_doc1, self.text_doc2],
            "spreadsheet": [self.spreadsheet_doc1, self.spreadsheet_doc2],
            "presentation": [self.presentation_doc1, self.presentation_doc2]
        }

    def run(self):
        traverse_instance_tree(self.root_doc)
        # traverse_class_tree(type(self.root_doc))
        # dictionary_collection(self.doc_dict)


def traverse_instance_tree(instance):
    print(f"(enter) Class : {type(instance).__name__} name: {instance.name}")
    for child in instance.children:
        traverse_instance_tree(child)
    print(f"(exit) Class: {type(instance).__name__} name: {instance.name}")

def traverse_class_tree(cls):
    print(cls.__name__)
    for subclass in cls.__subclasses__():
        traverse_class_tree(subclass)

def dictionary_collection(doc_dict):
    for doc_type in doc_dict:
        for doc in doc_dict[doc_type]:
            if doc_type == "text":
                print(doc.read())
            elif doc_type == "spreadsheet":
                print(doc.read())
            elif doc_type == "presentation":
                print(doc.read())

def main():
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()