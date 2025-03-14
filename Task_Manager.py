import json 
import hashlib
import os

class TaskManager:
    def __init__(self):
        self.users_file="users.json"
        self.tasks_dir= "tasks"
        self.current_user=None
        
        if not os.path.exists(self.tasks_dir):
            os.makedirs(self.tasks_dir)
            
        
        if not os.path.exists(self.users_file):
            with open(self.users_file,"w") as file:
                json.dump({},file)
    
    def hide_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

#User Authentication:
    #Registration
    def register(self):
        username = input("Enter a new username: ") # Enter Username
        password = input("Enter password: ") # Enter password
        
        with open(self.users_file,"r") as file:
            users = json.load(file)
            
        if username in users:
            print("Username already exists! Try logging in.")
            return False
        
        users[username] = self.hide_password(password)
        
        with open(self.users_file,"w") as file:
            json.dump(users,file)
            
        print("Registration successful! You can now login.")
        return True
    
    #Login
    
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        with open(self.users_file,"r") as file:
            users=json.load(file)
            
        if username in users and users[username]==self.hide_password(password):
            print(f"Welcome! {username}")
            self.current_user=username
            return True
        else:
            print("Invalid username or password")
            return False
    #Return task path for logged in user   
    def get_task_file(self):
        return os.path.join(self.tasks_dir,f"{self.current_user}.json")
    
    #Return the task
    def load_task(self):
        task_file = self.get_task_file()
        if os.path.exists(task_file):
            with open(task_file,"r") as file:
                return json.load(file)
        return []
    
    #Save the Task
    def save_task(self,tasks):
        task_file=self.get_task_file()
        with open(task_file,"w") as file:
            json.dump(tasks, file)
    
    #Add the task        
    def add_task(self):
        if not self.current_user:
            print("Please log in first!")
            return
        
        task_description = input("Enter task description: ")
        tasks = self.load_task()
        task_id = len(tasks)+1
        tasks.append({"id":task_id,"description":task_description,"status":"Pending"})
        self.save_task(tasks)
        print(f"Task added successfully with ID: {task_id}")
        
    # Viewing the Task    
    def view_task(self):
        if not self.current_user:
            print("Please log in first!")
            return
        
        tasks=self.load_task()
        if not tasks:
            print("No task found.")
            return
        
        print("\n Your Tasks:")
        
        for task in tasks:
            status = "Completed" if task["status"]=="Completed" else "Pending"
            print(f"ID: {task['id']} | {task['description']} [{status}]")
            
     #Task marked as completed       
    def mark_as_complete(self):
        if not self.current_user:
            print("Please log in first!")
            return
        
        tasks= self.load_task()
        if not tasks:
            print("No task found.")
            return
        
        self.view_task()
        try:
            task_id = int(input("Enter task ID to mark as completed: "))
            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = "Completed"
                    self.save_task(tasks)
                    print("Task marked as completed!")
                    return
                
            print("Task ID not found!")
        except ValueError:
            print("Please enter a valid number!")
    
    #Delete the task        
    def delete_task(self):
        if not self.current_user:
            print("Please log in first!")
            return
        
        tasks= self.load_task()
        if not tasks:
            print("No task found.")
            return
        
        self.view_task()
        
        try:
            task_id = int(input("Enter task ID to delete: "))
            new_tasks = [tasks for task in tasks if task["id"]!=task_id]
            
            if len(new_tasks) == len(tasks):
                print("Task ID not found!")
                
            else:
                self.save_task(new_tasks)
                print(f" Task {task_id} deleted!")
        except ValueError:
            print("Please enter a valid number!")
    
    #Registration Menu
    
    def menu(self):
        while True:
            print("\n Task Manager")
            print("1 Register")
            print("2 login")
            print("3 Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.register()
            elif choice == '2':
                if self.login():
                    self.task_menu()
            elif choice == '3':
                print("Exiting...Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
    
    #Task Manager Menu
    
    def task_menu(self):
        while self.current_user:
            print("\n Task Manager (Logged in as: "+ self.current_user + ")")
            print("1 Add Task")
            print("2 View Tasks")
            print("3 Mark Task as Completed")
            print("4 Delete task")
            print("5 Logout")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.mark_as_complete()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Logging out..")
                self.current_user=None
                break
            else:
                print("Invalid choice! Please try again.")
                
if __name__ == "__main__":
    manager = TaskManager()
    manager.menu()
                