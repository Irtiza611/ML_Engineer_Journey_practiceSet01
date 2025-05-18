import json
import os

data =[]

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(title, desc):
    tasks = load_tasks()
    task_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        'id' : task_id,
        'title' : title,
        'desc' : desc,
        'completed' : False 
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("New task has been added ")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print("zTask deleted.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "task completed" if task["completed"] else "not completed"
        print(f"[{task['id']}] {status} {task['title']} - {task['desc']}")

def mark_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
            return
    print("Task not found.")

def update_task(task_id, new_title, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            task["desc"] = new_description
            save_tasks(tasks)
            print("Task updated.")
            return
    print("Task not found.")


print("Welcome to To Do App ")
while True:
    choice = int(input(""" What do you want to do
                        1. Add task
                        2. Delete task
                        3. Update task
                        4. Mark task
                        5. View all tasks 
                        6. Exit
                    """))

    if choice == 1:
        title = input("enter title of the task : ")
        desc = input("enter description of task")
        add_task(title, desc)

    elif choice == 2:
        task_id = int(input("enter the id of task to be deleted : "))
        delete_task(task_id)

    elif choice == 3:
        task_id = int(input("enter the id of task to be updated : "))
        new_title = input("enter new title of the task : ")
        new_desc = input("enter new description of task")
        update_task(task_id, new_title, new_desc)

    elif choice == 4:
        task_id = int(input("Enter task ID to mark as completed: "))
        mark_task(task_id)

    elif choice == 5:
        view_tasks()

    elif choice == 6:
        print("Thank you ")
        break

    else:
        print("quiting the app. Thank you")
        break