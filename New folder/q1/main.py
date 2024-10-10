# main.py

from manager import Manager

def main():
    manager = Manager()

    while True:
        print("\nToDo List Manager")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display Tasks")
        print("4. Task Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_id = input("Enter task ID (numeric): ")
            try:
                manager.add_task(title, description, task_id)
            except ValueError as e:
                print(e)

        elif choice == '2':
            task_id = input("Enter task ID to mark as done: ")
            manager.mark_task_done(task_id)

        elif choice == '3':
            manager.display_tasks()

        elif choice == '4':
            manager.task_summary()

        elif choice == '5':
            print("Exiting the ToDo List Manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()