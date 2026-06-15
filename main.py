from dataclasses import dataclass
import argparse
import json
import os

@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    priority: int = 1

todos = []

TODO_FILE = os.path.expanduser('~/.todos.json')

def add_todo(title, priority=1):
    new_id = len(todos) + 1
    todos.append(Todo(id=new_id, title=title, priority=priority))
    save_todos()

def remove_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    save_todos()

def list_todos():
    for todo in todos:
        status = '✓' if todo.done else '✗'
        print(f'{todo.id}: {todo.title} [{status}] (Priority: {todo.priority})')

def mark_done(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            todo.done = True
            break
    save_todos()

# Load todos from file if it exists
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'r') as f:
        todos = json.load(f)

# Save todos to file

def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

# Main CLI logic would go here
