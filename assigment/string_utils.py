"""14. Implement a Python module named string_utils.py containing functions for string manipulation, such as
reversing and capitalizing strings."""

def reverse_string(s: str) -> str:
   
    return s[::-1]

def capitalize_string(s: str) -> str:
  
    return s.title()

def uppercase_string(s: str) -> str:
    
    return s.upper()

def lowercase_string(s: str) -> str:
   
    return s.lower()

def count_vowels(s: str) -> int:
    
    
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    # Test the functions
    test_string = "Hello, World!"
    
    print("Original String:", test_string)
    print("Reversed String:", reverse_string(test_string))
    print("Capitalized String:", capitalize_string(test_string))
    print("Uppercase String:", uppercase_string(test_string))
    print("Lowercase String:", lowercase_string(test_string))
    print("Vowel Count:", count_vowels(test_string))
