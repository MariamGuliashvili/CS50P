employees = ["John Smith", "Alice Johnson", "Bob Brown", "Emma Davis"]

def print_employee_list():
    print("List of Employees:")
    for idx, employee in enumerate(employees, start=1):
        print(f"{idx}. {employee}")

def add_employee():
    new_employee = input("Enter the name and surname of the new employee: ")
    employees.append(new_employee)
    print(f"{new_employee} has been added to the employee list.")

def remove_employee():
    print_employee_list()
    if employees:
        try:
            index = int(input("Enter the number of the employee to remove: "))
            if 0 <= index < len(employees):
                removed_employee = employees.pop(index)
                print(f"{removed_employee} has been removed from the employee list.")
            else:
                print("Invalid employee number. Please enter a valid employee number.")
        except ValueError:
            print("Invalid input. Please enter a valid employee number.")
    else:
        print("The employee list is empty.")

def main():
    while True:
        print_employee_list()
        print("\nOptions:")
        print("1. Remove an employee")
        print("2. Add a new employee")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            remove_employee()
        elif choice == "2":
            add_employee()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
