import datetime
import os


class Task:
    def __init__(self, title, description=None, dueDate=None) -> None:
        current_date_time = datetime.datetime.now()
        self.title = title
        self.description = description
        self.date_created = current_date_time.strftime("%d-%m-%Y")
        self.time_created = current_date_time.time().strftime("%I:%M:%S %p")
        self.due_date = dueDate
        self.completed = "Not Completed!"


task1 = Task(title="Study Math", description="Study Limits", dueDate="20-03-2024")
task2 = Task(title="Study C Language", description="Study About Pointers")


all_tasks = [task1, task2]


def add_task():

    ask_task_title = input("Enter your task title: ")

    if not ask_task_title:
        print("You have not entered anything!")
        return False

    else:
        ask_task_description = input("Enter your task description(if any)\n>")

        try:
            taskDueDate = input("Date Format: 'dd-mm-yyyy(full-year)'\nEnter Due Date(optional): ")
            dueDate = datetime.datetime.strptime(taskDueDate, "%d-%m-%Y").strftime("%d-%m-%Y") if taskDueDate else None

        except ValueError:
            dueDate = None
            print("Wrong Date Format!")

        task_description = ask_task_description if ask_task_description else None
        task = Task(title=ask_task_title, description=task_description, dueDate=dueDate)

        all_tasks.append(task)
        print("Your task has been added! :)")

        input("Press Enter to Continue...")
        return True


def clear_screen():
    os.system("cls")


def delete_task(all_tasks: list):
    print_all_task(all_tasks)

    ask_index = input("Enter the number of the task you want to remove: ")

    if not ask_index.isdigit():
        print("Invalid! Enter a integer.")
    
    elif int(ask_index) > len(all_tasks):
        print(f"There are only {len(all_tasks)} tasks!")

    else:
        ask_index = int(ask_index) - 1
        del all_tasks[ask_index]
        print("Task is now removed from the list")
        print()

    input("Press Enter to Continue...")


def print_all_task(all_tasks):
    print("ALL THE TASKS".center(50, "-"))

    for index, task in enumerate(all_tasks, start=1):
        print(f"{index}. {task.title}")
        print(f"Task Description: {task.description}")
        print(f"Task Due Date: {task.due_date}")
        print(f"Task Status: {task.completed}")
        print()

    print("-"*50)


def mark_as_completed(all_tasks: list):
    print_all_task(all_tasks)

    ask_task = input("Enter the task number you want to mark as completed: ").strip()

    while (not ask_task.isdigit()) or (int(ask_task) > len(all_tasks)):
        print("Invalid! Please enter a appropriate input.")
        ask_task = input("Enter the task number you want to mark as completed: ").strip()

    ask_task = int(ask_task) - 1
    all_tasks[ask_task].completed = "Completed!"

    if all_tasks[ask_task].completed != "Not Completed!":
        print(f"Task: '{all_tasks[ask_task].title}' is now marked as Completed! :)")

        delete = input("Do you also wish to remove it from the list ?(y/n)").lower()
        if delete == "y":
            del all_tasks[ask_task]
            print("Task is now removed from the list")

    else:
        print("The task is already marked as completed.")

    print()

    input("Press Enter to Continue...")


while True:
    clear_screen()

    print("TO DO LIST".center(50, "-"))
    print("1. ADD A TASK")
    print("2. DELETE A TASK")
    print("3. MARK A TASK AS COMPLETED")
    print("4. PRINT ALL THE TASKS")
    print("5. EXIT")
    print("TO DO LIST".center(50, "-"))

    choice = input("Enter your choice: ").strip()

    while not choice.isdigit():
        choice = input("Invalid! Please enter a integer value\nEnter your choice: ").strip()

    choice = int(choice)

    match choice:
        case 1:
            add_task()
        case 2:
            delete_task(all_tasks)
        case 3:
            mark_as_completed(all_tasks)
        case 4:
            print_all_task(all_tasks)
            input("Press Enter to Continue...")
        case 5:
            break
        case _:
            print("Invalid Input! Enter a number between 1-5")
            input("Press Enter to Continue...")
