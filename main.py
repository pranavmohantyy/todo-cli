from dataclasses import dataclass
import argparse
import json
import os

dataclass
class Todo:
    id: int
    title: str
    done: bool = False

todos = []

TODO_FILE = os.path.expanduser('~/.todos.json')


def add_todo(title):
    new_id = len(todos) + 1
    todos.append(Todo(id=new_id, title=title))
    save_todos()


def remove_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    save_todos()


def list_todos():
    for todo in todos:
        status = '✓' if todo.done else '✗'
        print(f'{todo.id}: {todo.title} [{status}]')


def mark_done(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            todo.done = True
            break
    save_todos()


def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump([todo.__dict__ for todo in todos], f)


def load_todos():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            todos = [Todo(**data) for data in json.load(f)]


def main():
    load_todos()
    # add argparse functionality here

if __name__ == '__main__':
    main()