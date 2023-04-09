import functions
import PySimpleGUI as sGUI

label = sGUI.Text("Type in a to-do")
input_box = sGUI.InputText(tooltip="Enter todo", key="todo")
add_button = sGUI.Button("Add")
list_box = sGUI.Listbox(values=functions.get_todos(), key="todos",
                        enable_events=True, size=(45, 10))
edit_button = sGUI.Button("Edit")

window = sGUI.Window('My To-Do App',
                     layout=[[label], [input_box, add_button], [list_box, edit_button]],
                     font=('Helvetica', 20))
while True:
    event, values = window.read()
    
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sGUI.WIN_CLOSED:
            break

window.close()