import json
import matplotlib.pyplot as plt

# Print welcome messages
print("Welcome to the Personal Finance Tracker!")
print("You can add income, add expenses, and generate reports.")

# Initialize variables
income = []
expenses = []
savings = 0
transactions = []

# Function to get user input
def get_input(prompt):
    return input(prompt)

# Function to display output
def display_output(message):
    print(message)

# Function to add income
def add_income(amount, description):
    global savings
    income.append({'amount': amount, 'description': description})
    savings += amount
    transactions.append({'type': 'income', 'amount': amount, 'description': description})

# Function to add expense
def add_expense(amount, description):
    global savings
    expenses.append({'amount': amount, 'description': description})
    savings -= amount
    transactions.append({'type': 'expense', 'amount': amount, 'description': description})

# Function to calculate savings
def calculate_savings():
    return savings

# Main menu function
def main_menu():
    while True:
        choice = get_input("Choose an option: (1) Add Income, (2) Add Expense, (3) View Savings, (4) Generate Report, (5) Plot Expenses, (6) Exit: ")
        if choice == '1':
            amount = float(get_input("Enter income amount: "))
            description = get_input("Enter income description: ")
            add_income(amount, description)
        elif choice == '2':
            amount = float(get_input("Enter expense amount: "))
            description = get_input("Enter expense description: ")
            add_expense(amount, description)
        elif choice == '3':
            display_output(f"Total Savings: {calculate_savings()}")
        elif choice == '4':
            generate_report()
        elif choice == '5':
            plot_expenses()
        elif choice == '6':
            display_output("Thank you for using the Personal Finance Tracker!")
            save_transactions()
            break
        else:
            display_output("Invalid option. Please try again.")

# Function to save transactions to a file
def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

# Function to load transactions from a file
def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []

# Function to categorize expenses
def categorize_expenses():
    categories = {}
    for expense in expenses:
        category = expense.get('category', 'Uncategorized')
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']
    return categories

# Function to generate a report
def generate_report():
    categories = categorize_expenses()
    for category, amount in categories.items():
        print(f"{category}: {amount}")

# Function to plot expenses using Matplotlib
def plot_expenses():
    categories = categorize_expenses()
    labels = categories.keys()
    sizes = categories.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

# Function to add income with error handling
def add_income(amount, description):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Income must be positive.")
        income.append({'amount': amount, 'description': description})
        global savings
        savings += amount
        transactions.append({'type': 'income', 'amount': amount, 'description': description})
    except ValueError as e:
        print(f"Error: {e}")

# Function to add expense with error handling
def add_expense(amount, description):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Expense must be positive.")
        expenses.append({'amount': amount, 'description': description})
        global savings
        savings -= amount
        transactions.append({'type': 'expense', 'amount': amount, 'description': description})
    except ValueError as e:
        print(f"Error: {e}")

# Load previous transactions if available
load_transactions()

# Start the main menu
main_menu()

# Print closing message
print("Thank you for using the Personal Finance Tracker!")
