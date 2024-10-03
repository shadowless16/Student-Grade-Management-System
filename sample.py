print("Hello welcome to To Do List App")

option = input("Select one of the following options \n1. Add new task \n2. Remove task \n3. View all task \nSelect one of the following options: ")

todo = {}

def add_task():
    task = input("What would you like to add: ")
    todo[task] = {"info": {}}
    print(f"{task} has been added to yor todo list.")

def remove_task():
    pass

def view_task():
    pass

match option:
    case 1:
        add_task()
    case 2:
        remove_task()
    case 3:
        view_task()