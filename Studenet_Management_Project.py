# Student Management System using Python (Beginner Level)
# This program allows users to add, view, search, and remove student records using file handling.

# Function to display all student records
def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if students:
                print("\nList of Students:")
                for student in students:
                    print(student.strip())  # Removing extra spaces
            else:
                print("\nNo student records found.")
    except FileNotFoundError:
        print("\nFile not found. No students added yet.")

# Function to add a new student
def add_student():
    name = input("\nEnter Student Name: ").strip()
    if name:
        with open("students.txt", "a") as file:
            file.write(name + "\n")  # Writing student name to file
        print(f"Student '{name}' added successfully!")
    else:
        print("Invalid input! Name cannot be empty.")

# Function to search for a student
def search_student():
    search_name = input("\nEnter Student Name to Search: ").strip().lower()
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            found = any(student.strip().lower() == search_name for student in students)
            if found:
                print(f"Student '{search_name}' found in the system.")
            else:
                print(f"Student '{search_name}' not found.")
    except FileNotFoundError:
        print("\nFile not found. No students added yet.")

# Function to remove a student
def remove_student():
    remove_name = input("\nEnter Student Name to Remove: ").strip().lower()
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
        with open("students.txt", "w") as file:
            new_students = [student for student in students if student.strip().lower() != remove_name]
            file.writelines(new_students)
        if len(students) > len(new_students):
            print(f"Student '{remove_name}' removed successfully!")
        else:
            print(f"Student '{remove_name}' not found.")
    except FileNotFoundError:
        print("\nFile not found. No students added yet.")

# Main Program Loop
while True:
    print("\n📌 Student Management System")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        print("\nExiting Program. Have a nice day! 😊")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
