from dataclasses import dataclass
import argparse
import json
import os
from datetime import datetime

dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    priority: int = 1
    due_date: str = None

todos = []

TODO_FILE = os.path.expanduser('~/.todos.json')

def add_todo(title, priority=1, due_date=None):
    new_id = len(todos) + 1
    todos.append(Todo(id=new_id, title=title, priority=priority, due_date=due_date))
    save_todos()

def remove_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    save_todos()

def list_todos(done=None, pending=None, overdue=None):
    now = datetime.now()
    for todo in todos:
        if done is not None and todo.done != done:
            continue
        if pending is not None and todo.done == False:
            continue
        if overdue is not None:
            if todo.due_date:
                due_date = datetime.strptime(todo.due_date, '%Y-%m-%d')
                if due_date >= now:
                    continue
        print(f'[{todo.id}] {todo.title} - Priority: {todo.priority} - Due: {todo.due_date}')