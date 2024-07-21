# To do list - TASK 1

to_do = []
def create_tasks():
    print("Enter your tasks: (Enter 0 to exit)")
    add = ''
    while add != '0':
        add = input()
        to_do.append(add)
    to_do.remove('0')
    print("Tasks added succesfully!")
    print("-----------------------------------------")

def update_tasks():
    print("TO DO LIST:")
    for i in to_do:
        print(i)
    update = int(input("Enter the task number to update\n"))
    updated = input("Enter the task to be updated:\n")
    to_do[update-1] = updated
    print("Task updated successfully!")
    print("-----------------------------------------")

def track_tasks():
    print("TO DO LIST:")
    for i in to_do:
        print(i)
    print("-----------------------------------------")

task = ''
while task != 0:
    task = int(input("Choose any one option:\n1.Create tasks\n2.Update tasks\n3.Track tasks\n(Enter 0 to exit)\n"))
    if task == 1:
        create_tasks()
    elif task == 2:
        update_tasks()
    elif task == 3:
        track_tasks()
    elif task == 0:
        print("Goodbye!")
    