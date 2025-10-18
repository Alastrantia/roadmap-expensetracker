import argparse

parser = argparse.ArgumentParser(prog="expense-tracker", description="A simple command-line expense tracker.")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

add_parser = subparsers.add_parser("add", help="Add a new expense")
add_parser.add_argument("--description", type=str, required=True, help="Description of the expense")
add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

list_parser = subparsers.add_parser("list", help="List all expenses")

summary_parser = subparsers.add_parser("summary", help="Show the sum of all expenses to see how much they all cost together")
summary_parser.add_argument('--month', type=int, required=False, help="Toggle to only show sum for a certain month, 1-12")

delete_parser = subparsers.add_parser("delete", help="Delete a specified expense")
delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense")
