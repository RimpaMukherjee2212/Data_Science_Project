# Data_Science_Projects

--------------------------------------------------------------Project 1 - Persoanl Expense Tracker-----------------------------------------------------------------------------------

This code is a Personal Expense Tracker that helps user to record, view and manage their daily expenses. This  also includes a budgeting feature to help users monitor their spending habits.
Steps followed in the Code:
•	Adding Expenses: Users can input expense details such as date,category,amount and description. These details will be stored in CSV file(expenses.csv) for storage.
•	Viewing Expenses: This tracker displays all recorded expenses, calculates the total spent, and warns user if there are any incomplete or invalid entries.
•	Budget Tracking: Users can set a monthly budget and system calculates the remaining budget while altering them if they exceed the limit.
•	Data Storage: These expenses are saved in a CSV file that ensuring that data is retained even after the program is closed. Upon startup, the program loads existing expense records from the file.
•	Interactive Menu: A simple option based menu allows users to navigate between different options.

--------------------------------------------------------------Project 2 - Task Manager with User Authentication------------------------------------------------------------------------------

This code is Task Manger with user authentication Security. Once logged in, users can create, view, update, and delete their tasks. Each user’s tasks should be stored separately, and only the authenticated user can access their tasks. This also includes file handling to store user credentials by Hash the password for better security.
Steps followed in the Code:
•	Registration : Users enter a unique username and password and password are hashed for security. data is stored in “users.json”.
•	Login : Users enter their username and password. Credentials are verified from users.json. If correct, the user gains access to the Task Manager.
•	Add Task : Users enter a task description. The system assigns a unique task ID and sets the status to Pending. Task is stored in a JSON file specific to the user(tasks/{username}.json).
•	View Tasks : Retrieves all tasks for the logged-in user. Displays task ID, description, and status(Pending/Completed).
•	Mark Task as Completed : Users select a task ID. The status changes to Completed.
•	Delete Task : Users select a Task ID to delete. This task is removed from the file.
•	User Data(users.json) : Stores user credentials in a dictionary {username: hashed_password}.
•	Task Data (tasks/{username}.json) : Stores each user’s tasks separately for privacy.
•	Authentication Menu : Users must register or log in before accessing tasks.
•	Task Menu : After login, users see options to add, view, mark, or delete tasks.
•	Logout: Allows users to securely exit and prevent unauthorized access.


