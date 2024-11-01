x = "core.txt"

def addtask():
    task = input("Enter your task: ")
    if not task:
        print("Enter the task please!!!")
    else:
        with open(x, "a") as f:
            f.write(task + "\n")

def removetask():
    with open(x, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("No tasks to remove.")
        return
    
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")
        
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task.strip()}" removed successfully.')

            with open(x, "w") as f:
                f.writelines(tasks)
        else:
            print("Invalid task number.")
    
    except ValueError:
        print("Please enter a valid task number.")

def read():
    with open(x, "r") as f:
        tasks = f.read()
    
    if not tasks:
        print("Nothing to display!!!")
    else:
        print("\n-----YOUR LISTED TASKS ARE-----")
        print(tasks, "\n")

def main():
    print("\n-----TO DO LIST-----")
    
    while True:
        print("\nEnter 1 for adding a task")
        print("Enter 2 for deleting a task")
        print("Enter 3 for reading tasks")
        print("Enter 4 for exiting the program")
        
        try:
            choice = int(input("Enter the task you want to do: "))
            
            if choice == 1:
                addtask()
            elif choice == 2:
                removetask()
            elif choice == 3:
                read()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
