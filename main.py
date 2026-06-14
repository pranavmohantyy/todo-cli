from dataclasses import dataclass
import argparse

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


def list_todos():
    for todo in todos:
        status = '✓' if todo.done else '✗'
        print(f'{todo.id}: {todo.title} [{status}]')


def mark_done(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            todo.done = True
            break


def main():
    parser = argparse.ArgumentParser(description='Todo CLI manager')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('title', type=str, help='Title of the todo')

    done_parser = subparsers.add_parser('done')
    done_parser.add_argument('id', type=int, help='ID of the todo to mark as done')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('id', type=int, help='ID of the todo to remove')

    list_parser = subparsers.add_parser('list', help='List all todos')

    args = parser.parse_args()

    if args.command == 'add':
        add_todo(args.title)
    elif args.command == 'done':
        mark_done(args.id)
    elif args.command == 'remove':
        remove_todo(args.id)
    elif args.command == 'list':
        list_todos()

if __name__ == '__main__':
    main()