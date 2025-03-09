class Task:
    def __init__(self, title, desciption):
        self.title = title
        self.description = desciption
        self.status = "todo"
        
    def change_status(self, status):
        self.status = status