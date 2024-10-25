class Task:
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed

    def complete_task(self):
        self.is_completed = True

    def get_status(self):
        if self.is_completed:
            return 'Completed'
        else:
            return 'Pending'
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        print(self.tasks)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f'{task.description}: {task.get_status()}')

# Programa Principal
task1 = Task('Finish Homework')
task2 = Task('Do Laundry')
manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)
manager.view_tasks()