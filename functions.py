FILEPATH = "todo.txt"

def get_todos(filename=FILEPATH):
    with open(filename, 'r') as open_file:
        todos_local = open_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as write_file:
        write_file.writelines(todos_arg)
