from dataclasses import dataclass
import argparse
import json
import os
from datetime import datetime
from colorama import Fore, Style

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


def list_todos():
    for todo in todos:
        color = Style.RESET_ALL
        if todo.due_date and datetime.strptime(todo.due_date, '%Y-%m-%d') < datetime.now():
            color = Fore.RED
        elif todo.priority > 1:
            color = Fore.YELLOW
        if todo.done:
            color = Style.DIM
        print(f'{color}{todo.id}. {todo.title} (Priority: {todo.priority}, Due: {todo.due_date}){Style.RESET_ALL}')
...