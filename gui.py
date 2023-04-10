import functions
import PySimpleGUI as sGUI
import time

sGUI.theme("DarkPurple4")

clock = sGUI.Text('', key="clock")
label = sGUI.Text("Type in a to-do")
input_box = sGUI.InputText(tooltip="Enter todo", key="todo")
add_button = sGUI.Button("Add")
list_box = sGUI.Listbox(values=functions.get_todos(), key="todos",
                        enable_events=True, size=(45, 10))
edit_button = sGUI.Button("Edit")
complete_button = sGUI.Button("Complete")
exit_button = sGUI.Button("Exit")

window = sGUI.Window('My To-Do App',
                     layout=[[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                     font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sGUI.popup("Please select an item first.", font=("Helvetica", 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sGUI.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sGUI.WIN_CLOSED:
            break

window.close()