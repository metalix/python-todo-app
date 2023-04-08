import functions
import PySimpleGUI as sG

label = sG.Text("Type in a to-do")
input_box = sG.InputText(tooltip="Enter todo")
add_button = sG.Button("Add")

window = sG.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()