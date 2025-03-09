from lib.task import Task

class TasksManager:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def add_task(self, new_task: Task):
        self.tasks.append(new_task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def get_all_tasks(self):
        return self.tasks