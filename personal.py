import json
import os

# File name to store the data
DATA_FILE = 'budget_data.json'

# Function to load data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

# Function to save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Function to display main menu
def display_menu():
    print("\n==== Budget Tracker ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. Exit")

# Function to add income
def add_income(data):
    amount = float(input("Enter income amount: "))
    data['income'] += amount
    print("Income added successfully!")

# Function to add expense
def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print("Expense added successfully!")

# Function to view budget
def view_budget(data):
    print("\n==== Budget Overview ====")
    print("Total Income:", data['income'])
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    print("Total Expenses:", total_expenses)
    print("Remaining Budget:", data['income'] - total_expenses)
    print("\n==== Expense Analysis ====")
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        categories[category] = categories.get(category, 0) + amount
    for category, amount in categories.items():
        print(category + ":", amount)

# Main function
def main():
    data = load_data()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_budget(data)
        elif choice == '4':
            save_data(data)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
