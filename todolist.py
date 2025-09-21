import json
import os

FILENAME = "tasks.json"

# ----------------- Data Handling -----------------
def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    """Load tasks from JSON file, return list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# ----------------- UI Functions -----------------
def show_menu():
    """Display the main menu."""
    print("\n--- Simple To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    """Display all tasks with status."""
    if not tasks:
        print("No tasks available.")
    else:
        print(f"\nYou have {len(tasks)} task(s):")
        for i, task in enumerate(tasks, 1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

# ----------------- Features -----------------
def add_task(tasks):
    """Add one or multiple tasks, validate input."""
    titles = input("Enter task(s) (separate multiple tasks with commas): ").strip()
    if not titles:
        print("Task title cannot be empty!")
        return

    added = 0
    for title in [t.strip() for t in titles.split(",") if t.strip() != ""]:
        tasks.append({"title": title, "done": False})
        added += 1

    save_tasks(tasks)
    print(f"{added} task(s) added!")

def mark_task_done(tasks):
    """Mark a task as done, allow cancel."""
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to mark as done (0 or c to cancel): ").strip()
    if choice in ("0", "c", "C"):
        print("Cancelled.")
        return

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_num = int(choice)
    if 1 <= task_num <= len(tasks):
        if tasks[task_num - 1]["done"]:
            print("Task already marked as done!")
        else:
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
    else:
        print("Invalid task number. Please try again.")

def delete_task(tasks):
    """Delete a task, allow cancel."""
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete (0 or c to cancel): ").strip()
    if choice in ("0", "c", "C"):
        print("Cancelled.")
        return

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_num = int(choice)
    if 1 <= task_num <= len(tasks):
        deleted = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{deleted['title']}' deleted.")
    else:
        print("Invalid task number. Please try again.")

# ----------------- Main Program -----------------
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
