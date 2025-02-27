import uuid
from datetime import datetime, timezone

# Expense class
# Task 1: Implement an __init__ method to initialize the attributes
class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())  
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)  
        self.updated_at = self.created_at 
    
    # Task 2: Implement an update method that allows updating the title and/or amount of the expense. The updated_at attribute should be automatically set to the current UTC timestamp whenever an update occurs.
    def update(self, title: str = None, amount: float = None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc) 
    
    # Task 3: Implement a to_dict method that returns a dictionary representation of the expense.
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

# Expense Database clas2
class ExpenseDatabase:
    # Task 1: Implement an __init__ method to initialize the expenses list.
    def __init__(self):
        self.expenses = []
    
    # Task 2: Implement methods to:
    # i.) Add an expense to the database.
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    # ii.) Remove an expense from the database.
    def remove_expense(self, expense_id: str):
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
    
    # iii.) Get an expense by ID.
    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
    
    # iv.) Get expenses by title (returning a list).
    def get_expense_by_title(self, title: str):
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]

    # Task 3: Create a to_dict method that returns a list of dictionaries representing each expense in the database.
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

# Testing the project 
if __name__ == "__main__":
    db = ExpenseDatabase()

    # Create expenses
    expense_one = Expense("Groceries", 104000.0)
    expense_two = Expense("Electricity Bill", 10000.0)
    expense_three = Expense("House rent", 550000.0)
    expense_four = Expense("Savings", 750000.0)

    # Add expenses to the database
    db.add_expense(expense_one)
    db.add_expense(expense_two)
    db.add_expense(expense_three)
    db.add_expense(expense_four)

    # Update an expense
    expense_one.update(amount=5500.0)

    # Retrieve by ID
    fetched_expense = db.get_expense_by_id(expense_one.id)
    print(f"Fetched Expense: {fetched_expense.to_dict() if fetched_expense else 'Not found'}")

    # Retrieve by title
    expenses_by_title = db.get_expense_by_title("House rent")
    print(f"Expenses by Title: {[exp.to_dict() for exp in expenses_by_title]}")

    # Remove an expense
    db.remove_expense(expense_two.id)

    # View all expenses
    print("All Expenses:", db.to_dict())
