import sqlite3
import argparse

# Database connection and CRUD operation functions remain the same...

# CLI argument parsing
def create_parser():
    parser = argparse.ArgumentParser(description='Manage friend information in the SQLite database.')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new friend')
    add_parser.add_argument('name', help='Name of the friend')
    add_parser.add_argument('email', help='Email of the friend')
    add_parser.add_argument('phone_number', help='Phone number of the friend', nargs='?')
    add_parser.add_argument('address', help='Address of the friend', nargs='?')
    add_parser.add_argument('birthdate', help='Birthdate of the friend', nargs='?')

    # List command
    list_parser = subparsers.add_parser('list', help='List all friends')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update friend information')
    update_parser.add_argument('id', type=int, help='ID of the friend to update')
    update_parser.add_argument('name', help='New name of the friend')
    update_parser.add_argument('email', help='New email of the friend')
    update_parser.add_argument('phone_number', help='New phone number of the friend', nargs='?')
    update_parser.add_argument('address', help='New address of the friend', nargs='?')
    update_parser.add_argument('birthdate', help='New birthdate of the friend', nargs='?')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a friend')
    delete_parser.add_argument('id', type=int, help='ID of the friend to delete')

    return parser

# Main function to execute the CLI
def main():
    init_db()
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'add':
        add_friend(args.name, args.email, args.phone_number, args.address, args.birthdate)
    elif args.command == 'list':
        list_friends()
    elif args.command == 'update':
        update_friend(args.id, args.name, args.email, args.phone_number, args.address, args.birthdate)
    elif args.command == 'delete':
        delete_friend(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()