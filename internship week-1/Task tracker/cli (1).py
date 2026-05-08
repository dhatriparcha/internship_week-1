import requests

BASE = "http://127.0.0.1:5000"

def show_tasks():
    res = requests.get(f"{BASE}/view")
    tasks = res.json()["tasks"]

    if not tasks:
        print("\n  No tasks yet.\n")
        return

    print("\n" + "-" * 45)
    print(f"  {'ID':<6} {'TITLE':<25} {'STATUS'}")
    print("-" * 45)
    for task in tasks:
        print(f"  {task['id']:<6} {task['title']:<25} {task['status']}")
    print("-" * 45 + "\n")

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Update status")
    print("5. Delete task")
    print("6. Quit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter task title: ")
        res = requests.post(f"{BASE}/add", json={"title": title})
        print(res.json()["message"])

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        task_id = int(input("Enter task ID to edit: "))
        new_title = input("Enter new title: ")
        res = requests.put(f"{BASE}/edit/{task_id}", json={"title": new_title})
        print(res.json()["message"])

    elif choice == "4":
        show_tasks()
        task_id = int(input("Enter task ID: "))
        print("Statuses: Pending / In Progress / Done")
        new_status = input("Enter new status: ")
        res = requests.patch(f"{BASE}/status/{task_id}", json={"status": new_status})
        print(res.json()["message"])

    elif choice == "5":
        show_tasks()
        task_id = int(input("Enter task ID to delete: "))
        res = requests.delete(f"{BASE}/delete/{task_id}")
        print(res.json()["message"])

    elif choice == "6":
        break

    print()

