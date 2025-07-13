class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_index):
        if task_index <= 0 or task_index > len(self.tasks):
            print("Invalid task index.")
        else:
            del self.tasks[task_index - 1]
            print(f"Task {task_index} has been removed.")

    def mark_task_complete(self, task_index):
        if task_index <= 0 or task_index > len(self.tasks):
            print("Invalid task index.")
        else:
            self.tasks[task_index - 1] += " (completed)"
            print(f"Task {task_index} has been marked as completed.")


def main():
    todo_list = ToDoList()
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_task_complete(task_index)
        elif choice == "5":
            print("Exiting the to-do list app.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()