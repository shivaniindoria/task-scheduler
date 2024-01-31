# Task scheduler that allows users to add, edit, and delete tasks.
# Python's datetime module to set reminders and deadlines for tasks.
# Basic functionalities like listing all tasks, marking tasks as completed, and sorting tasks by date.
# Store tasks in a text file. 

import os
import datetime

class TaskManager:
    def __init__(self, file_name="tasks.txt"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    task_info = line.strip().split(',')
                    task = {
                        'title': task_info[0],
                        'deadline': datetime.datetime.strptime(task_info[1], '%Y-%m-%d %H:%M:%S'),
                        'completed': task_info[2] == 'True'
                    }
                    tasks.append(task)
        return tasks

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['title']},{task['deadline']},{task['completed']}\n")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "[X]" if task['completed'] else "[ ]"
                print(f"{index}. {status} {task['title']} - Deadline: {task['deadline']}")

    def add_task(self, title, deadline):
        new_task = {
            'title': title,
            'deadline': deadline,
            'completed': False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def edit_task(self, task_index, new_title, new_deadline):
        task = self.tasks[task_index - 1]
        task['title'] = new_title
        task['deadline'] = new_deadline
        self.save_tasks()
        print(f"Task {task_index} edited successfully.")

    def delete_task(self, task_index):
        deleted_task = self.tasks.pop(task_index - 1)
        self.save_tasks()
        print(f"Task '{deleted_task['title']}' deleted successfully.")

    def mark_as_completed(self, task_index):
        self.tasks[task_index - 1]['completed'] = True
        self.save_tasks()
        print(f"Task {task_index} marked as completed.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task_manager.list_tasks()

        elif choice == '2':
            title = input("Enter task title: ")
            deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM:SS): ")
            deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d %H:%M:%S')
            task_manager.add_task(title, deadline)

        elif choice == '3':
            task_manager.list_tasks()
            task_index = int(input("Enter the task number to edit: "))
            new_title = input("Enter new task title: ")
            new_deadline_str = input("Enter new task deadline (YYYY-MM-DD HH:MM:SS): ")
            new_deadline = datetime.datetime.strptime(new_deadline_str, '%Y-%m-%d %H:%M:%S')
            task_manager.edit_task(task_index, new_title, new_deadline)

        elif choice == '4':
            task_manager.list_tasks()
            task_index = int(input("Enter the task number to delete: "))
            task_manager.delete_task(task_index)

        elif choice == '5':
            task_manager.list_tasks()
            task_index = int(input("Enter the task number to mark as completed: "))
            task_manager.mark_as_completed(task_index)

        elif choice == '6':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
