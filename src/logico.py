# src/task_manager.py

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} - {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return task
        return None
