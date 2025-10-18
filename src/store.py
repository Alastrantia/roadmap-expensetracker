import json, os

def save_json(expenses):
    with open("expenses.json", "w") as f:
        f.write(json.dumps(expenses))


def load_json():
    if not os.path.exists("expenses.json"):
        with open("expenses.json", "w") as f:
            f.write("[]")

    with open("expenses.json", "r+") as f:
        content = f.read().strip()
        if not content:
            f.seek(0)
            f.write("[]")
            f.truncate()
            content = "[]"
        return json.loads(content)