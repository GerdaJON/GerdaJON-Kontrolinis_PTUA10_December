from datetime import datetime

tasks_list = []
# tasks_dict = {}
def add_task():
    while True:
        task = input("Enter a task: ")
        date_str = input("Enter the date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        tasks_list.append((task, date))
        tasks_append = input("Add another task? (y/n): ")
        if tasks_append == 'No' or 'n' or 'N':
            break
        return add_task()

def tasks_display():
    print("Here are your tasks:")
    for task, date in tasks_list:
        print(f"{task} is Due on {date}")

def mark_compl():
    pass
    # tasks_list["value1"] += "(COMPLETED)"

def delete_task():
    print(tasks_display())
    what_to_delete = int(input('Which job should be removed?'))
    # tasks_list.remove(what_to_delete)
    del tasks_list[what_to_delete]

def tasks_search():
    pass

def edit_task():
    pass

def to_do_list():
    while True:
        print("To-Do List Options:\n1. Add task\n2. Display tasks\n3. Mark task as completed\n4. Delete task\n5. Search task\n6. Edit task\n7. QUIT")
        option = int(input('Enter your choice: '))
        if option == 1:
            print(add_task())
        elif option == 2:
            print(tasks_display())
        elif option == 3:
            print(mark_compl())
        elif option == 4:
            print(delete_task())
        elif option == 5:
            print(tasks_search())
        elif option == 6:
            print(edit_task())
        elif option == 7:
            print('Exiting task list!')
            break
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
    return to_do_list()
print(to_do_list())