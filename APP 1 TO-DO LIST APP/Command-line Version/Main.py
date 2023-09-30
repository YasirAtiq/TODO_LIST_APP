### My Version of the app: TO-DO LIST
### This is the command line version
## Importing...
import json
import time

##Telling the time
now = time.strftime("%d-%b-%Y %I:%M:%S")
print(f"It is {now}")

##Creating or reading TO-DO LIST
# Reading the TO-DO LIST from "todo_list.json"
try:
    with open("todo_list.json", "r") as file:
        todo = json.load(file)
        todo = list(todo)
# Creating an empty TO-DO LIST
except FileNotFoundError:
    print("The TO-DO LIST was not found")
    todo = []
    todo = list(todo)


##Defining:
# Adding task
def add_task(task):
    task = task[4:]
    todo.append(task)


# Completing Task
def complete_task(task):
    task = task[9:]
    try:
        todo.remove(task)
    except ValueError:
        print(f"""The task "{task}" doesn't exists""")


# Showing TO-DO LIST
def show():
    try:
        for x in range(0, len(todo) + 1):
            print(f"{x + 1}. {todo[x]}\n")
    except IndexError:
        pass


## Processing user input
while True:
    # User Input
    ui = input(
        """Type:
1. "add (task)" to add a task.
2. "show" to show the TO-DO LIST
3. "complete (task)" to complete a task
4. "exit" to exit:\n""")
    # Processing the command
    if ui[:4] == "add " or ui[:4] == "Add ":
        add_task(ui)
        continue
    elif ui == "show" or ui == "Show":
        show()
        continue
    elif ui[:9] == "complete " or ui[:9] == "Complete ":
        complete_task(ui)
        continue
    elif ui == "exit" or ui == "Exit":
        break
    else:
        print("Invalid task given")
        continue

##Saving the new or modified TO-DO LIST
with open("todo_list.json", "w") as file:
    todo = json.dump(todo, file)
