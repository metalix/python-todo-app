import functions
import PySimpleGUI as sGUI

label = sGUI.Text("Type in a to-do")
input_box = sGUI.InputText(tooltip="Enter todo", key="todo")
add_button = sGUI.Button("Add")

window = sGUI.Window('My To-Do App',
                     layout=[[label], [input_box, add_button]],
                     font=('Helvetica', 20))
while True:
    event, values = window.read()
    
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sGUI.WIN_CLOSED:
            break

window.close()