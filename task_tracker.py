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
        try:
            with open(self.JSON_PATH, 'r', encoding='UTF-8') as tasks_json:
                tasks = json.load(tasks_json)

            return tasks
        
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return 0

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return 0
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0
    
    # Function to write JSON file
    def write_json(self, tasks):
        try:
            with open(self.JSON_PATH, 'w', encoding='UTF-8') as tasks_json:
                json.dump(tasks, tasks_json, indent=4, ensure_ascii=False)

            return 1
        
        except IOError as e:
            print(f"I/O error occurred while writing to the file. {e}")
            return 0
        
        except ValueError as e:
            print(f"Value error occurred while serializing data. {e}")
            return 0
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0

    # Function to get the current date in ISO format
    def get_current_date(self):
        try:
            current_date = datetime.datetime.now()
            current_date = current_date.isoformat()

            return current_date
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
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

    # Function to list all tasks or filter by status
    # Valid statuses: all, todo, in-progress, done
    def list_tasks(self, status):
        tasks = self.read_json()

        valid_statuses = ['all', 'todo', 'in-progress', 'done']

        if status not in valid_statuses:
            print(f"'{status}' is an invalid status. Please choose 'all', 'todo', 'in-progress' or 'done'.")
            return None
        
        if status == 'all':
            for task in tasks:
                print(f'\n{task}\n')

        else:
            for task in tasks:
                if task['status'] == status:
                    print(f'\n{task}\n')

task_tracker = TaskTracker()

task_tracker.list_tasks('done')
