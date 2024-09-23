import os
import json
import datetime
import argparse


class TaskTracker:
    def __init__(self) -> None:

        self.JSON_PATH = 'tasks.json'
        self.create_json()

    # Create a JSON file to store tasks if the file does not exist
    def create_json(self):
        try:
            if not os.path.exists(self.JSON_PATH):
                with open(self.JSON_PATH, 'w') as tasks_json:
                    json.dump([], tasks_json)
            
                return (1, "Success: JSON file created.")
            
            return (0, "Info: JSON file already exists.")
        
        except PermissionError:
            return (0, "No permission to create JSON file.")
        
        except OSError as e:
            return (0, f"OS Issue ocorred - {e}")

    # Function to read JSON file
    def read_json(self):
        try:
            with open(self.JSON_PATH, 'r', encoding='UTF-8') as tasks_json:
                tasks = json.load(tasks_json)

            return tasks
        
        except FileNotFoundError as e:
            return (0, f"File not found - {e}")

        except json.JSONDecodeError as e:
            return (0, f"Error decoding JSON - {e}")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
    
    # Function to write JSON file
    def write_json(self, tasks):
        try:
            with open(self.JSON_PATH, 'w', encoding='UTF-8') as tasks_json:
                json.dump(tasks, tasks_json, indent=4, ensure_ascii=False)

            return (1, 'Success: JSON written.')
        
        except OSError as e:
            return (0, f"Error occurred while writing to the file - {e}")
        
        except ValueError as e:
            return (0, f"Value error occurred while serializing data - {e}")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")

    # Function to get the current date in ISO format
    def get_current_date(self):
        try:
            current_date = datetime.datetime.now()
            current_date = current_date.isoformat()

            return current_date
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
    
    # Verify and get the last task ID from the JSON file
    def get_last_id(self):
        try:
            tasks = self.read_json()
            
            # Check if the reading returned an error code.
            if isinstance(tasks, list):
                if tasks:
                    last_id = max(task['id'] for task in tasks)
                else:
                    last_id = 0
                return last_id
            else:
                return tasks  # Return the error code from read_json.
        
        except KeyError:
            return (0, "Error: 'id' key not found in a task.")
        
        except TypeError:
            return (0, "Error: Invalid data type encountered.")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
    
    # Add a new task to the JSON file
    def add_task(self, description):
        try:
            last_id = self.get_last_id()

            new_id = last_id + 1
            description = description

            current_date = self.get_current_date()

            task_format = {"id": new_id, 
                            "description": description, 
                            "status": 'todo', # Status "todo" set as default.
                            "createdAt": current_date, 
                            "updateAt": current_date}

            tasks = self.read_json()

            tasks.append(task_format)

            self.write_json(tasks)

            print(f"Task added successfully (ID: {new_id})")

            return (1, f"Success: Task added successfully (ID: {new_id})")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")

    # Function for deleting a task
    def delete_task(self, task_id):     
        try:   
            tasks = self.read_json()

            tasks = [task for task in tasks if task['id'] != task_id]

            self.write_json(tasks)

            return (1, f"Success: Task with ID {task_id} deleted.")

        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")

    # Function to update tasks descriptions
    def update_task(self, task_id, new_description):
        try:
            tasks = self.read_json()

            current_date = self.get_current_date()

            tasks = [
                {**task, "description": new_description, "updateAt": current_date} 
                if task['id'] == task_id else task for task in tasks
            ]

            self.write_json(tasks)
            
            return (1, f"Success: Task with ID {task_id} updated.")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
        
    # Function to mark task as in-progress
    def make_in_progress(self, task_id):
        try:
            tasks = self.read_json()

            current_date = self.get_current_date()

            tasks = [
                {**task, "status": 'in-progress', "updateAt": current_date} 
                if task['id'] == task_id else task for task in tasks
            ]

            self.write_json(tasks)

            return (1, f"Success: Task with ID {task_id} updated.")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
        
    # Function to mark task as done
    def make_done(self, task_id):
        try:
            tasks = self.read_json()

            current_date = self.get_current_date()

            tasks = [
                {**task, "status": 'done', "updateAt": current_date} 
                if task['id'] == task_id else task for task in tasks
            ]

            self.write_json(tasks)

            return (1, f"Success: Task with ID {task_id} updated.")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")

    # Function to list all tasks or filter by status
    # Valid statuses: all, todo, in-progress, done
    def list_tasks(self, status):
        try:
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

            return (1, f"Success: Tasks listed.")
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")
        
    @staticmethod
    def cli():

        parser = argparse.ArgumentParser(description='Task Tracker CLI')

        # Defining the subcommands for the CLI
        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # Command to add a task
        parser_add = subparsers.add_parser('add-task', help='Add a new task')
        parser_add.add_argument('description', type=str, help='Task description')

        # Command to delete a task
        parser_delete = subparsers.add_parser('delete-task', help='Delete a task')
        parser_delete.add_argument('task_id', type=int, help='Task ID to delete')

        # Command to update a task
        parser_update = subparsers.add_parser('update-task', help='Update task description')
        parser_update.add_argument('task_id', type=int, help='Task ID to update')
        parser_update.add_argument('description', type=str, help='New task description')

        # Command to list tasks
        parser_list = subparsers.add_parser('list-tasks', help='List tasks by status')
        parser_list.add_argument('status', type=str, choices=['all', 'todo', 'in-progress', 'done'], help='Task status to list')

        # Command to mark a task as in-progress
        parser_in_progress = subparsers.add_parser('make-in-progress', help='Mark task as in-progress')
        parser_in_progress.add_argument('task_id', type=int, help='Task ID to mark as in-progress')

        # Command to mark a task as done
        parser_done = subparsers.add_parser('make-done', help='Mark task as done')
        parser_done.add_argument('task_id', type=int, help='Task ID to mark as done')

        # Parsing the arguments provided by the user
        args = parser.parse_args()

        # Creating an instance of TaskTracker
        task_tracker = TaskTracker()

        try:
            # Executing the function corresponding to the command
            if args.command == 'add-task':
                task_tracker.add_task(args.description)
            elif args.command == 'delete-task':
                task_tracker.delete_task(args.task_id)
            elif args.command == 'update-task':
                task_tracker.update_task(args.task_id, args.description)
            elif args.command == 'list-tasks':
                task_tracker.list_tasks(args.status)
            elif args.command == 'make-in-progress':
                task_tracker.make_in_progress(args.task_id)
            elif args.command == 'make-done':
                task_tracker.make_done(args.task_id)
            else:
                parser.print_help()
        
        except Exception as e:
            return (0, f"An unexpected error occurred - {e}")


if __name__ == "__main__":
    TaskTracker.cli()
