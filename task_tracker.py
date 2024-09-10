import os
import json
import datetime

class TaskTracker:
    def __init__(self) -> None:

        self.JSON_PATH = 'tasks.json'
        self.create_json()

    # Create a JSON file to store tasks if the file does not exist
    def create_json(self):
        if not os.path.exists(self.JSON_PATH):
            with open(self.JSON_PATH, 'w') as tasks_json:
                json.dump([], tasks_json)
        
            return 1
        
        return 0

    # Function to read JSON file
    def read_json(self):
        with open(self.JSON_PATH, 'r', encoding='UTF-8') as tasks_json:
            tasks = json.load(tasks_json)

        return tasks
    
    # Function to write JSON file
    def write_json(self, tasks):
        with open(self.JSON_PATH, 'w', encoding='UTF-8') as tasks_json:
            json.dump(tasks, tasks_json, indent=4, ensure_ascii=False)

    # Function to get the current date in ISO format
    def get_current_date(self):
        current_date = datetime.datetime.now()
        current_date = current_date.isoformat()

        return current_date
    
    # Verify and get the last task ID from the JSON file
    def get_last_id(self):        
        tasks = self.read_json()

        if tasks:
            last_id = max(task['id'] for task in tasks)
        else:
            last_id = 0

        return last_id
    
    # Add a new task to the JSON file
    def add_task(self, description):
        last_id = self.get_last_id()

        new_id = last_id + 1
        description = description

        current_date = self.get_current_date()

        task_format = {"id": new_id, 
                        "description": description, 
                        "status": 'todo', 
                        "createdAt": current_date, 
                        "updateAt": current_date}

        tasks = self.read_json()

        tasks.append(task_format)

        self.write_json(tasks)

        print(f"Task added successfully (ID: {new_id})")

    # Function for deleting a task
    def delete_task(self, task_id):        
        tasks = self.read_json()

        tasks = [task for task in tasks if task['id'] != task_id]

        self.write_json(tasks)

    # Function to update tasks descriptions
    def update_task(self, task_id, new_description):
        tasks = self.read_json()

        current_date = self.get_current_date()

        tasks = [
            {**task, "description": new_description, "updateAt": current_date} 
            if task['id'] == task_id else task for task in tasks
        ]

        self.write_json(tasks)

    # Function to mark task as in-progress
    def make_in_progress(self, task_id):
        tasks = self.read_json()

        current_date = self.get_current_date()

        tasks = [
            {**task, "status": 'in-progress', "updateAt": current_date} 
            if task['id'] == task_id else task for task in tasks
        ]

        self.write_json(tasks)

    # Function to mark task as done
    def make_done(self, task_id):
        tasks = self.read_json()

        current_date = self.get_current_date()

        tasks = [
            {**task, "status": 'done', "updateAt": current_date} 
            if task['id'] == task_id else task for task in tasks
        ]

        self.write_json(tasks)

task_tracker = TaskTracker()

task_tracker.make_done(8)
