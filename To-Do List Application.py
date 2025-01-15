def display_menu():
    print('''To-Do List Menu:
    1. Add Task
    2. Remove Task
    3. View Tasks
    4. Exit
    ''')

user_todo_task = []

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        user_todo_task.append(task)
        print(f"Task added: {task}")

    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in user_todo_task:
            user_todo_task.remove(task)
            print(f"Task removed: {task}")
        else:
            print("Task not found.")

    elif choice == '3':
        if user_todo_task:
            print("Your tasks:")
            for idx, task in enumerate(user_todo_task, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your to-do list is empty.")

    elif choice == '4':
        print("Thank you for using the To-Do List application. Goodbye!")
        break

    else:
        print("Please select a correct option (1-4).")
