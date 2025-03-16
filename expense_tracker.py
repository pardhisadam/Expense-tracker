import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']}: {expense['description']}")

    def get_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            summary[category] = summary.get(category, 0) + amount
        
        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., food, transport, entertainment): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.get_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
