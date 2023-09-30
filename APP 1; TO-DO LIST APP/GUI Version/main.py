### My Version of the app: TO-DO LIST
### This is the GUI version Frontend
##Importing...
import PySimpleGUI as p

from Backend import *

##Elements:
# Text Box
Input = p.InputText(tooltip="Enter Here:", key="input")
# Label
label = p.Text("TO-DO Item:")
# List of TO-DOs
listbox = p.Listbox(values=read_todos(), key="list", enable_events=True, size=[45, 10])
# Buttons:
# a. Add Button
add = p.Button("Add")
# b. Edit Button
edit = p.Button("Edit")

##Layout of the window
layout = [[label], [Input, add], [listbox, edit]]

##Main Window
window = p.Window("TO-DO LIST APP",
                  layout=layout,
                  font=("Comic Sans MS", 16))

##Main program
while True:
    ##Getting event and values
    event, val = window.read()
    print(event)
    print(val)
    match event:
        case "Add":
            ##Defining what happens when "Add" button is pressed.
            todos = read_todos()
            new_todo = val["input"] + "\n"
            todos.append(new_todo)
            modifying_todo(todos)
            window["list"].update(values=todos)
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
        case "list":
            ##Making the selected object in list in the todo 
            window["input"].update(value=val['list'][0])
        case p.WIN_CLOSED:
            break

##When closed
window.close()
