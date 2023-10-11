import json
import os
from datetime import datetime

# Initialize an empty list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    global expenses
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the expense category: ")
    description = input("Enter a description: ")
    amount = float(input("Enter the expense amount: "))
    
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Function to list expenses
def list_expenses():
    global expenses
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: ${expense['amount']}")

# Function to calculate total expenses
def calculate_total_expenses():
    global expenses
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total}")

# Function to save data to a JSON file
def save_data():
    global expenses
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

# Function to load data from a JSON file
def load_data():
    global expenses
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            print("Data loaded successfully!")

# Main menu
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Calculate Total Expenses")
    print("4. Save Data")
    print("5. Load Data")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        calculate_total_expenses()
    elif choice == "4":
        save_data()
    elif choice == "5":
        load_data()
    elif choice == "6":
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")