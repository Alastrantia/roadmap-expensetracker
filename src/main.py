import sys, store
from commands import *
from datetime import date

today = date.today().strftime("%Y-%m-%d")

# load it all from the store
expenses = store.load_json()

# commands are defined in commands.py
args = parser.parse_args()

def final_print(message):
    print(message)
    store.save_json(expenses)
    sys.exit(0)

if args.command == "add":
    expenses.append({
        "ID": len(expenses) + 1,
        "Date": today,
        "Description": args.description,
        "Amount": args.amount
    })
    final_print(f"Expense added successfully (ID: {len(expenses)})")
elif args.command == "list":
    print(" ID  Date       Description  Amount")
    for expense in expenses:
        print(f" {expense["ID"]}  {expense["Date"]}  {expense["Description"]}  ${expense["Amount"]}")
elif args.command == "summary":
    total_amount = 0
    for expense in expenses:
        if not args.month:
            total_amount += expense["Amount"]
        else:
            # access the middle value of the date, which is the month i hopes
            month = int(expense["Date"].split("-")[1])
            total_amount += expense["Amount"] if month == args.month else 0

    final_print(f"Total expenses: ${total_amount:.2f}")
elif args.command == "delete":
    target_id = args.id
    index = next((index for index, dictionary in enumerate(expenses) if dictionary["ID"] == target_id), None)
    if index == None:
        final_print("Could not find expense with specified ID")
    expenses.pop(index)
    final_print("Expense deleted successfully")

else:
    parser.print_help()