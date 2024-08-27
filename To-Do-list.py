import json

def load_tasks(filename='tasks.json'):
    try:
        with open("tasks.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

# Display all tasks
def display_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx + 1}. {task['description']} - {status}")

# Add a new task
def add_task(tasks, description):
    tasks.append({'description': description, 'completed': False})

# Mark a task as complete
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True

# Remove a task
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Save and exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == '4':
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

