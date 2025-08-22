def show_menu():
    print("\n--- Simple To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            print("Task added!")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            task_num = int(input("Enter task number to mark as done: "))
            tasks[task_num - 1]["done"] = True
            print("Task marked as done!")

        elif choice == "4":
            view_tasks(tasks)
            task_num = int(input("Enter task number to delete: "))
            deleted = tasks.pop(task_num - 1)
            print(f"Task '{deleted['title']}' deleted.")

        elif choice == "5":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
