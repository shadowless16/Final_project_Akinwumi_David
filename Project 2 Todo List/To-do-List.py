print("Hello welcome to To Do List App")

# Todo List array
todo = []


#Add task function
def add_task():
    task = input("What would you like to add: ")
    todo.append(task)
    print(f"{task} has been added to yor todo list.")
    print(todo)

#remove task function
def remove_task():
    task = input("What would you like to remove: ")
    todo.remove(task)
    print(f"{task} has been removed from your todo list")

#view task function
def view_task():
    if len(todo) == 0:
        print("Your to-do list is empty!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todo, start=1):
            print(f"{i}. {task}")

#exit task function
def exit_program():
    print("Exiting Program....👋👋👋👋👋")


#conditonal loop to run the menu option repeatedly
while True:
        option = int(input("Select one of the following options \n1. Add new task \n2. Remove task \n3. View all tasks \n4. Exit Program \nSelect one of the following options: "))

        match option:
            case 1:
                add_task()
            case 2:
                remove_task()
            case 3:
                view_task()
            case 4:
                exit_program()
                break
            case _:
                print("Invalid option pls select an option between 1-4.")
