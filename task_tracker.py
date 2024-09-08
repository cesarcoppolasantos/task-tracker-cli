import os
import json
import datetime

class MyTodo:
    def __init__(self) -> None:

        self.JSON_PATH = 'tasks.json'
        self.create_json()

    # Create a json to store tasks if json file not exists
    def create_json(self):        

        if not os.path.exists(self.JSON_PATH):
            with open(self.JSON_PATH, 'w') as tasks_json:
                json.dump([], tasks_json)
        
            return 1
        
        return 0

    # Verify the last task id in json file
    def get_last_id(self):

        with open(self.JSON_PATH, 'r', encoding="UTF-8") as tasks_json:

            tasks = json.load(tasks_json)
        
            if tasks:
                last_id = max(task['id'] for task in tasks)
            else:
                last_id = 0

        return last_id
    
    # Add new task to json file
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



todo = MyTodo()

todo.add_task('test description', 'pending')
