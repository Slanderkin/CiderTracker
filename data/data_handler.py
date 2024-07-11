import json

class DataHandler:
    
    def __init__(self):
        self.rows = None
        self.header = None
    
    def SaveData(self):
        with open('cache\data.json', 'w') as f:
            data = {
                'header': self.header,
                'rows': self.rows,
            }
            json.dump(data, f)
            
    def LoadData(self):
        file = open('cache\data.json', 'r')
        data = json.load(file)
        
        if 'rows' in data:
            self.rows = data['rows']
        else:
            self.LoadDefaultRows()
        if 'header' in data:
            self.header = data['header']
        else:
            self.LoadDefaultHeader()
            
    def LoadDefaultHeader(self):
        self.header = [
            {'field': 'name', 'editable': True, 'sortable': True},
            {'field': 'age', 'editable': True},
            {'field': 'id'},
        ]
    def LoadDefaultRows(self):
        self.rows = [
            {'id': 0, 'name': 'Alice', 'age': 18},
            {'id': 1, 'name': 'Bob', 'age': 21},
            {'id': 2, 'name': 'Carol', 'age': 20},
        ]
            