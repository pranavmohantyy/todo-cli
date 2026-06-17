from dataclasses import dataclass
import json
import os

@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    priority: int = 1
    due_date: str = None

todos = []
TODO_FILE = os.path.expanduser('~/.todos.json')

def load_todos():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            todos = json.load(f)


def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)


def add_todo(title, priority=1, due_date=None):
    new_id = len(todos) + 1
    todos.append(Todo(id=new_id, title=title, priority=priority, due_date=due_date))
    save_todos()


def remove_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    save_todos()