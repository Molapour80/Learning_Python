# manager.py

from task import Task

class Manager:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, title, description, task_id):
        if task_id in self.tasks:
            raise ValueError("Task ID must be unique.")
        new_task = Task(title, description, task_id)
        self.tasks[task_id] = new_task
        print(f"Task '{title}' added successfully.")

    def mark_task_done(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_done()
            print(f"Task ID {task_id} marked as done.")
        else:
            print("Task not found.")

    def display_tasks(self):
        for task in self.tasks.values():
            print(task)

    def task_summary(self):
        completed = sum(1 for task in self.tasks.values() if task.status)
        not_completed = len(self.tasks) - completed
        print(f"Total completed tasks: {completed}")
        print(f"Total not completed tasks: {not_completed}")