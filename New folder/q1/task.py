# task.py

from datetime import datetime

class Task:
    def __init__(self, title, description, task_id):
        if not task_id.isnumeric():
            raise ValueError("Task ID must be numeric.")
        self.title = title
        self.description = description
        self.task_id = task_id
        self.start_time = datetime.now()
        self.end_time = None
        self.status = False  

    def mark_done(self):
        self.status = True
        self.end_time = datetime.now()

    def __str__(self):
        return (f"Task ID: {self.task_id}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Start Time: {self.start_time}\n"
                f"End Time: {self.end_time if self.end_time else 'Not completed'}\n"
                f"Status: {'Done' if self.status else 'Not done'}\n")