# To-Do List with CSV Export
import csv

tasks = []

def add_task(task):
    tasks.append(task)

def save_tasks():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])

while True:
    print("\n1. Add Task\n2. Save and Exit")
    choice = input("Choose option: ")
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        save_tasks()
        print("Tasks saved to tasks.csv")
        break
