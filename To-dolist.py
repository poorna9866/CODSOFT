import os

tasks = []

def add_task(description):
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f'Task "{description}" added.')

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. {task['description']} - {status}")

def update_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print(f'Task "{tasks[index]["description"]}" marked as completed.')
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        print(f'Task "{task["description"]}" deleted.')
    else:
        print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            description = input("Enter the task description: ").strip()
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter the task number to mark as completed: ").strip()) - 1
                update_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter the task number to delete: ").strip()) - 1
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
