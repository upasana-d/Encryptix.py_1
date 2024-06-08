import json
import os

# File to store the to-do list
TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task_description):
    tasks.append({'description': task_description, 'completed': False})
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f"{idx + 1}. {task['description']} [{status}]")

def mark_task_completed(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_description = input("Enter the task description: ")
            add_task(tasks, task_description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
