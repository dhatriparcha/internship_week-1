tasks = []
status = {}

STATUSES = ["To Do", "In Progress", "Done", "On Hold"]

def show_tasks():
    print("\nYour tasks:")
    if not tasks:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks):
            print("{:<5} {:<20} {:<15}".format(i+1, task, status[task]))

def pick_status():
    for i, s in enumerate(STATUSES):
        print(f"{i+1}. {s}")
    choice = int(input("Pick a status (1-4): ")) - 1
    return STATUSES[choice]

def add_task():
    task = input("Task name: ")
    tasks.append(task)
    status[task] = pick_status()
    show_tasks()

def edit_task():
    i = int(input("Task number to edit: ")) - 1
    del status[tasks[i]]
    tasks[i] = input("New name: ")
    status[tasks[i]] = pick_status()

def del_task():
    i = int(input("Task number to remove: ")) - 1
    del status[tasks[i]]
    tasks.pop(i)
    show_tasks()

while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        del_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")