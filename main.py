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

def list_todos():
    for todo in todos:
        status = '✓' if todo.done else '✗'
        overdue = ' (overdue)' if todo.due_date and datetime.strptime(todo.due_date, '%Y-%m-%d') < datetime.now() else ''
        print(f'{todo.id}: {status} {todo.title} [Priority: {todo.priority}]{overdue}')

    

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
    parser = argparse.ArgumentParser(description='Todo CLI')
    parser.add_argument('command', choices=['add', 'remove', 'list'])
    parser.add_argument('--title', type=str)
    parser.add_argument('--priority', type=int, default=1)
    parser.add_argument('--due_date', type=str)

    args = parser.parse_args()

    if args.command == 'add' and args.title:
        add_todo(args.title, args.priority, args.due_date)
    elif args.command == 'remove' and args.title:
        remove_todo(int(args.title))
    elif args.command == 'list':
        list_todos()


if __name__ == '__main__':
    main()