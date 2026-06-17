import argparse
from todo import add_todo, remove_todo, todos, load_todos
from colorama import Fore, Style

load_todos()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Todo CLI')
    parser.add_argument('--add', help='Add a new todo')
    parser.add_argument('--remove', type=int, help='Remove a todo by ID')
    parser.add_argument('--list', action='store_true', help='List all todos')
    args = parser.parse_args()

    if args.add:
        add_todo(args.add)
        print(Fore.GREEN + 'Todo added!' + Style.RESET_ALL)
    elif args.remove:
        remove_todo(args.remove)
        print(Fore.RED + 'Todo removed!' + Style.RESET_ALL)
    elif args.list:
        if todos:
            for todo in todos:
                status = '✓' if todo.done else '✗'
                print(f'{todo.id}: {todo.title} [{status}] (Priority: {todo.priority})')
        else:
            print('No todos found.')