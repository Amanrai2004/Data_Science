"""16. Write a Python program to create a text file named "employees.txt" and write the details of employees,
including their name, age, and salary, into the file."""


def write_employee_data(file_path: str, employee_data: list) -> None:
    
    with open(file_path, 'w') as file:
        for employee in employee_data:
            name, age, salary = employee
            file.write(f"Name: {name}, Age: {age}, Salary: ${salary:.2f}\n")

if __name__ == "__main__":
    
    employees = [
        ("Alice Smith", 30, 70000),
        ("Bob Johnson", 45, 85000),
        ("Charlie Brown", 28, 65000),
        ("Diana Prince", 35, 72000),
    ]
    
    # File path
    file_path = "employees.txt"
    
    write_employee_data(file_path, employees)
    
    print(f"Employee data has been written to {file_path}.")
