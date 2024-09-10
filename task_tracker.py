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

    # Verify and get the last task ID from the JSON file
    def get_last_id(self):

        with open(self.JSON_PATH, 'r', encoding="UTF-8") as tasks_json:

            tasks = json.load(tasks_json)
        
            if tasks:
                last_id = max(task['id'] for task in tasks)
            else:
                last_id = 0

        return last_id
    
    # Add a new task to the JSON file
    def add_task(self, description, status):
        last_id = self.get_last_id()

        new_id = last_id + 1

        description = description
        status = status

        date_now = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
        created_at = date_now
        update_at = date_now

        task = {"id": new_id, 
                "description": description, 
                "status":status, 
                "createdAt": created_at, 
                "updateAt": update_at}

        with open(self.JSON_PATH, 'r', encoding="UTF-8") as tasks_json:
            tasks = json.load(tasks_json)

        tasks.append(task)

        with open(self.JSON_PATH, 'w', encoding="UTF-8") as tasks_json:
            json.dump(tasks, tasks_json, indent=4, ensure_ascii=False)

        print(f"Task added successfully (ID: {new_id})")

    # Function to update task descriptions
    def update_task(self, task_id, new_description):
        with open(self.JSON_PATH, 'r', encoding="UTF-8") as tasks_json:
            tasks = json.load(tasks_json)

        for task in tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                date_now = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
                task['updateAt'] = date_now

        with open(self.JSON_PATH, 'w', encoding="UTF-8") as tasks_json:
            json.dump(tasks, tasks_json, indent=4, ensure_ascii=False)
                

task_tracker = TaskTracker()

task_tracker.update_task(1, 'updated description 1')
