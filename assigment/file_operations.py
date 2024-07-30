"""15. Write a Python module named file_operations.py with functions for reading, writing, and appending
data to a file."""


def read_file(file_path: str) -> str:

    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path: str, data: str) -> None:

    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path: str, data: str) -> None:
    
    with open(file_path, 'a') as file:
        file.write(data)

if __name__ == "__main__":
    
    test_file_path = "test_file.txt"
    
    print("Writing to file...")
    write_file(test_file_path, "Hello, World!\n")
    
    print("Reading from file...")
    content = read_file(test_file_path)
    print("File content:", content)
    
    print("Appending to file...")
    append_to_file(test_file_path, "Appending more data.\n")
    
    print("Reading from file again...")
    content = read_file(test_file_path)
    print("File content after appending:", content)
