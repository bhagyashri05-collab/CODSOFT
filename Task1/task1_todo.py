# This will hold all the tasks, each as a dictionary with a name and status
tasks = []

# Just showing the menu options to the user
def display_menu():
    print("\n--- My To-Do App ---")
    print("1. Show all tasks")
    print("2. Add new task")
    print("3. Mark task as complete")
    print("4. Remove a task")
    print("5. Quit")

# List everything currently in the task list
def list_tasks():
    if not tasks:
        print("Your list is empty!")  # No tasks? Just say that.
    else:
        print("\nYour Tasks:")
        for idx, item in enumerate(tasks, start=1):
            mark = "✔️" if item['done'] else "✖️"  # Show done/undone status
            print(f"{idx}) {item['title']} [{mark}]")

# This adds a task — super simple
def add_new_task():
    title = input("What's the task? ")
    tasks.append({'title': title, 'done': False})
    print(f"Task '{title}' added!")

# Mark a task as done by number (1-based index)
def complete_task():
    list_tasks()
    try:
        num = int(input("Which task number is done? "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            print("Nice! Task marked as complete.")
        else:
            print("That number doesn't match any task.")
    except ValueError:
        print("Please enter a valid number.")  # In case someone types letters

# Delete a task — careful! It’s gone after this
def remove_task():
    list_tasks()
    try:
        num = int(input("Which task to remove? "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed['title']}")
        else:
            print("That number doesn't match any task.")
    except ValueError:
        print("Enter a number only.")

# This is the main loop — it keeps the app running until you choose to quit
while True:
    display_menu()
    option = input("Choose something (1-5): ")

    if option == '1':
        list_tasks()
    elif option == '2':
        add_new_task()
    elif option == '3':
        complete_task()
    elif option == '4':
        remove_task()
    elif option == '5':
        print("Thanks for using To-Do App.")
        break
    else:
        print("Oops! Invalid input.")  # Handles any wrong choices
