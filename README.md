# Expense Tracker

the CLI expense tracker thing  
project link: https://roadmap.sh/projects/expense-tracker

## not done yet  
things missing:  
- proper file seperation
- ugly formatting on list command
- fix ID system
- you cant have negative expenses

i might do this at some point i kinda have to but eh

## Quick start

Add an expense:
```bash
$ uv run src/main.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ uv run src/main.py --description "Dinner" --amount 10
# Expense added successfully (ID: 2)
```

List all expenses:
```bash
$ uv run src/main.py list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10
```

Show totals:
```bash
$ uv run src/main.py summary
# Total expenses: $30
```

Delete an expense:
```bash
$ uv run src/main.py delete --id 2
# Expense deleted successfully

$ uv run src/main.py summary
# Total expenses: $20
```

Monthly summary:
```bash
$ uv run src/main.py summary --month 8
# Total expenses for August: $20
```

## Commands

- add
    - --description "TEXT"  : description of the expense
    - --amount NUMBER       : amount (numeric)
- list
    - Displays ID, date, description and amount for stored expenses
- summary
    - --month N (optional)  : show total for given month (1–12). Without --month shows grand total.
- delete
    - --id N               : delete expense by ID

## Notes

- Dates in the examples use YYYY-MM-DD.
- Amounts are displayed with a dollar sign ($) in examples; actual currency formatting depends on the tool configuration.
- Persisted storage and installation method depend on the packaged binary or distribution (see project-specific docs).

<!-- End of README -->