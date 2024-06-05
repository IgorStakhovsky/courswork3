import json

def load_operations():
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def show_last_5_transactions(operations):
    if len(operations) < 5:
        last_5_transactions = operations
    else:
        last_5_transactions = operations[-5:]

    for operations in last_5_transactions:
        print(f"{operations["date"]} {operations["description"]}")
        print(f"{operations["from"]} -> {operations["to"]}")
        print(f"{operations["amount"]} {operations["name"]}")
        print()
print(load_operations())