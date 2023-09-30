###Code Exercise making a height convertor
##Importing...
import PySimpleGUI as gui


##Define:
def convert(feet, inches):
    try:
        t_feet = feet + (inches / 12)
        metres = t_feet * 0.3048
        return metres
    except TypeError:
        print(f"Can't accept {type(t_inches)} format")


def valid(text):
    if len(text) == 1 and text in '+-':
        return True
    else:
        try:
            number = float(text)
            return True
        except:
            return False


###Elements:
##Labels
# "Enter feet: " label
feet_label = gui.Text("Enter feet: ")
# "Enter inches: " label
inches_label = gui.Text("Enter inches: ")
# Output label
output_label = gui.Text("", key="output")

##Input text blocks
# Feet input
feet_input = gui.InputText(key="feet")
# Inches input
inches_input = gui.InputText(key="inches")

##Conver button
convert_button = gui.Button("Convert")

##Layout
layout = [[feet_label, feet_input], [inches_label, inches_input], [convert_button, output_label]]

##Window
window = gui.Window("Convertor", layout=layout, font=("Comic Sans MS", 16))

##Main program
while True:
    event, value = window.read()
    match event:
        case "Convert":
            if valid(value["feet"]) and valid(value["inches"]):
                feet = float(value["feet"])
                inches = float(value["inches"])
                m = convert(feet, inches)
                window["output"].update(value=m)
        case gui.WIN_CLOSED:
            break
window.close()
