"""18. Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent
on various expenses listed in the file"""

def calculate_total_expenses(file_path: str) -> float:
    
    total = 0.0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into the name and amount, and strip any extra whitespace
                name, amount = line.split(',')
                amount = float(amount.strip())
                total += amount
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except ValueError:
        print(f"Error: Invalid format in the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return total

if __name__ == "__main__":
    # Define the path to the expenses file
    file_path = "expenses.txt"
    
    # Calculate the total expenses
    total_expenses = calculate_total_expenses(file_path)
    
    # Display the result
    print(f"The total amount spent on expenses is: ${total_expenses:.2f}")
