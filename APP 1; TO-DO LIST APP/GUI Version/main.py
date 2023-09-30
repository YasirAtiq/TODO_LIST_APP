### My Version of the app: TO-DO LIST
### This is the GUI version Frontend
##Importing...
import os

import PySimpleGUI as gui

from Backend import *

if os.path.exists("todo_list.txt"):
    with open("todo_list.txt", "w"):
        pass

##Time
t = time()
##Elements:
# Clock
clock = gui.Text(t, key="c")
# Text Box
Input = gui.InputText(tooltip="Enter Here:", key="input")
# Label
label = gui.Text("TO-DO Item:")
# List of TO-DOs
listbox = gui.Listbox(values=read_todos(), key="list", enable_events=True, size=[45, 10])
# Buttons:
# a. Add Button
add = gui.Button("Add")
# b. Edit Button
edit = gui.Button("Edit")
# c. Complete Button
complete = gui.Button("Complete")
# d. Exit Button
exit = gui.Button("Exit")
##Layout of the window
layout = [[clock], [label], [Input, add], [listbox, edit, complete, exit]]

##Main Window
window = gui.Window("TO-DO LIST APP",
                  layout=layout,
                  font=("Comic Sans MS", 16))

##Main program
while True:
    ##Getting event and values
    event, val = window.read(timeout=200)
    window["c"].update(value=time())
    match event:
        case "Add":
            ##Defining what happens when "Add" button is pressed.
            todos = read_todos()
            new_todo = val["input"] + "\n"
            todos.append(new_todo)
            modifying_todo(todos)
            window["list"].update(values=todos)
            window["c"].update(value=time())
        case "Edit":
            ##Defining what happens when "Edit" button is pressed.
            todos = read_todos()
            todo_edit = val["list"][0]
            new_todo = val["input"]
            todos.append(new_todo)
            index = todos.index(todo_edit)
            todos[index] = new_todo
            modifying_todo(todos)
            window["list"].update(values=todos)
            window["c"].update(value=time())
        case "Complete":
            ##Defining what happens when "Complete" button is pressed.
            todos = read_todos()
            todo_delete = val["list"][0]
            todos.remove(todo_delete)
            modifying_todo(todos)
            window["list"].update(values=todos)
            window["c"].update(value=time())

        case "list":
            ##Making the selected object in list in the todo 
            window["input"].update(value=val['list'][0])
            window["c"].update(value=time())

        case gui.WIN_CLOSED:
            break

        case "Exit":
            break

##When closed
window.close()
