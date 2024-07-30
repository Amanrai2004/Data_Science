
"""17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays
the contents of the file line by line."""

def read_and_display_file(file_path: str) -> None:
    
    try:
        with open(file_path, 'r') as file:
            # Read and display each line
            for line in file:
                print(line, end='')  # end='' to avoid double newlines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")

if __name__ == "__main__":
    # Define the path to the file
    file_path = "inventory.txt"
    
    # Read and display the contents of the file
    read_and_display_file(file_path)
