import csv
import os

class ExpenseTracker:
    def __init__(self,filename="expenses.csv"):
        self.filename=filename
        self.expenses = []
        self.monthly_budget = 0.0
        self.load_expenses()


#1. Add an expense:

    def add_expense(self):
        date = input("Enter the date (YYYY-MM-DD):")
        category = input("Enter the category:")
        try:
            amount = float(input("Enter the expense:"))
        except ValueError:
            print("Invalid amount! Please enter a valid number")
            return
        description = input("Enter the description:")
        
        expense={"date":date,"category":category,"amount":amount,"description":description}
        self.expenses.append(expense)
        self.save_expenses()
        print(f"expense added successfully")
#Set and track the budget:        
    def set_budget(self):
        try:
            self.monthly_budget = float(input("Enter your monthly budget:"))
            print(f"Monthly budget set to ${self.monthly_budget:.2f}")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
#Calculate the budget
    def calculate_total_expenses(self):
        
        if self.monthly_budget == 0:
            self.set_budget()
            
        total_spent = sum(expense["amount"] for expense in self.expenses)
        
        
        remaining_budget = self.monthly_budget-total_spent
        
        if remaining_budget < 0:
            print("Warning: You have exceeded your budget!")
        else:
            print(f" You have ${remaining_budget:.2f} left for the month.")
        
#2. View expenses:

    def view_expense(self):
        if not self.expenses:
            print("No record yet")
            return
        
        print("\nStored Expenses:")
        total_spent=0
        for idx,expense in enumerate(self.expenses,start=1):
            if not all(key in expense for key in ["date","category","amount","description"]):
                print(f"Warning: Skipping incomplete expense entry at index {idx}.")
                continue
            
            try:
                amount = float(expense["amount"])
            except ValueError:
                print(f"Warning: Skipping expense at index {idx} due to invalid amount foramt.")
                continue
            
            print(f"{idx}. Date: {expense['date']},Category: {expense['category']},"f"Amount: ${amount:.2f},Description: {expense['description']}")
            total_spent +=amount
        
        print(f"Total Amount Spent: ${total_spent:.2f}")
        
        if self.monthly_budget >0:
            print(f"Remaining Budget: ${self.monthly_budget - total_spent:.2f}")
            
#Save and load expenses:
    def save_expenses(self):
        with open(self.filename,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Description"])
            for expense in self.expenses:
                writer.writerow([expense["date"],expense["category"],expense["amount"],expense["description"]])
        print("Expenses saved successfully!")
    
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        row["amount"]= float(row["Amount"])
                        self.expenses.append(row)
                    except ValueError:
                        print(f"Warning! skipping invalid expense record: {row}")
#Intercative Menu 
    def menu(self):
        while True:
            print("\n Personal Expense Tracker")
            print(" 1 Add Expense")
            print(" 2 View Expense")
            print(" 3 Track  Budget")
            print(" 4 Save Expenses")
            print(" 5 Exit")
            
            choice = input("Enter your choice: ")
            
            if choice =="1":
                self.add_expense()
            elif choice == "2":
                self.view_expense()
            elif choice == "3":
                self.calculate_total_expenses()
            elif choice == "4":
                self.save_expenses()
            elif choice == "5":
                self.save_expenses()
                print("Exiting...Goodbye!")
                break
            else:
                print("Invalid choice! please try again.")
                
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
            
                