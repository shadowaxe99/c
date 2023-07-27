```python
import datetime
from typing import List, Dict

class Task:
    def __init__(self, id: int, name: str, description: str, due_date: datetime.datetime):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

    def update_status(self, status: str):
        self.status = status

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, id: int, name: str, description: str, due_date: datetime.datetime):
        new_task = Task(id, name, description, due_date)
        self.task_list.append(new_task)

    def remove_task(self, id: int):
        self.task_list = [task for task in self.task_list if task.id != id]

    def update_task_status(self, id: int, status: str):
        for task in self.task_list:
            if task.id == id:
                task.update_status(status)

    def get_tasks(self) -> List[Dict]:
        return [{"id": task.id, "name": task.name, "description": task.description, "due_date": task.due_date, "status": task.status} for task in self.task_list]
```