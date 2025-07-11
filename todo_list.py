todo_list={}
def show_menu():
    print("\n***** TO-DO LIST MENU *****")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Update tasks")
    print("4. Delete tasks")
def add_task():
    task_id=input("enter task id: ")
    task_name=input("enter task name: ")
    todo_list[task_id]=task_name
    print("task added successfully!")
def view_task():
    if not todo_list:
        print("no tasks in the list.")
    else:
        print("\nyour tasks:")
        for task_id,task_name in todo_list.items():
            print(f"ID: {task_id} - Task: {task_name}")
def update_task():
    task_id=input("enter task ID to update: ")
    if task_id in todo_list:
        new_name=input("enter new task name: ")
        todo_list[task_id]=new_name
        print("task updates successfully!")
    else:
        print("task ID not found")
def delete_task():
    task_id=input("enter the ID to delete: ")
    if task_id in todo_list:
        del todo_list[task_id]
        print("task deleted successfully!")
    else:
        print("task ID not found.")
while True:
    show_menu()
    choice=input("enter your choice (1-5): ")
    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        update_task()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("Goodbye!")
    else:
        print("invalid choice.Please enter a choice between 1 and 5.")

