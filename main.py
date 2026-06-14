from dataclasses import dataclass

@dataclass
class Todo:
    id: int
    title: str
    done: bool = False

todos = []

def add_todo(title):
    new_id = len(todos) + 1
    todos.append(Todo(id=new_id, title=title))

def remove_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]

def print_todos():
    for todo in todos:
        status = '✓' if todo.done else '✗'
        print(f'{todo.id}: {todo.title} [{status}]')

# Example usage
add_todo('Learn Python')
add_todo('Build a CLI')
print_todos()
remove_todo(1)
print_todos()