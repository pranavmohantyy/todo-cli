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


def stats():
    total = len(todos)
    completed = sum(1 for todo in todos if todo.done)
    pending = total - completed
    overdue = sum(1 for todo in todos if todo.due_date and datetime.strptime(todo.due_date, '%Y-%m-%d') < datetime.now() and not todo.done)
    print(f'Total: {total}, Pending: {pending}, Completed: {completed}, Overdue: {overdue}')

# add this to your command parsing logic
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Todo CLI')
    parser.add_argument('--stats', action='store_true', help='Show todo stats')
    args = parser.parse_args()

    if args.stats:
        stats()
    # add other command handlers here