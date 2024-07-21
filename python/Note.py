#Definition of Note class.

import uuid

class Note:
    def __init__(self):
        self.id = str(uuid.uuid1())
        self.content = ""
        self.tags = {"id": self.id}
    
    def getContent(self):
        return self.content
    
    def getId(self):
        return self.id
    
    def getTags(self):
        return self.tags