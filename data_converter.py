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