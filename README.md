# Task Tracker CLI

Task tracker is a project used to track and manage your tasks. A simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

## How to Install

1. Clone the repository to your local machine:

```bash
  git clone https://github.com/cesarcoppolasantos/task-tracker-cli.git
```

2. Navigate to the project directory:

```bash
  cd task-tracker-cli
```


## How to Run

1. To start the Task Tracker CLI, simply run the Python file where the TaskTracker class is implemented. In the terminal, use the following command:
### Windows
```bash
  python task_tracker.py <argument>
```
### Mac/Linux
```bash
  python3 task_tracker.py <argument>
```
2. Valid Arguments:
- add-task <task description> : Adds a new task.
- delete-task <task id> : Removes an existing task.
- update-task <task id> <new task description> : Updates the description of a task.
- list-task <"all"|"todo"|"in-progress"|"done"> : Lists tasks filtered by status.
- make-in-progress <task id> : Marks a task as "in-progress".
- make-done <task id> : Marks a task as "done".


3. When the project is executed for the first time, it will automatically create the tasks.json file in the execution directory. This file will be used to store your tasks.


## Examples of Use

- Add a task
```bash
  python3 task_tracker.py add-task <task description>
```

- Delete a task
```bash
  python3 task_tracker.py delete-task <task id>
```

- Update the description of a task
```bash
  python3 task_tracker.py update-task <task id> <new task description>
```

- List tasks
```bash
  python3 task_tracker.py list-tasks "all"
  ...

  python3 task_tracker.py list-tasks "todo"
  ...

  python3 task_tracker.py list-tasks "in-progress"
  ...

  python3 task_tracker.py list-tasks "done"
  ...
```

- Update the status of a task
```bash
  python3 task_tracker.py make-in-progress <task id>
  ...

  python3 task_tracker.py make-done <task id>
  ...
```
## Progress Checklist

- [x] Function to create a JSON file to store tasks
- [x] Functions to add, update, and delete tasks
- [x] Functions to mark tasks as "in-progress" or "done"
- [x] Functions to list all tasks, not done tasks, done tasks, and in-progress tasks
- [x] Handle errors and edge cases

#### Feel free to make any additional adjustments!

## Technology Stack

**Back-end:** 
- Python

## Reference

 - [Developer Roadmaps - Task Tracker CLI Project](https://roadmap.sh/projects/task-tracker)
