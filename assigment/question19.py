def count_words(file_path: str) -> dict:
    
    word_count = {}
    
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read()
            
            # Convert to lowercase and split into words
            words = content.lower().split()
            
            # Remove punctuation from words
            words = [word.strip(".,!?;:'\"()[]{}<>") for word in words]
            
            # Count occurrences of each word
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return word_count

def display_word_count(word_count: dict) -> None:
  
    for word in sorted(word_count.keys()):
        print(f"{word}: {word_count[word]}")

if __name__ == "__main__":
    # Define the path to the paragraph file
    file_path = "paragraph.txt"
    
    # Count the words in the file
    word_counts = count_words(file_path)
    
    # Display the word counts in alphabetical order
    display_word_count(word_counts)
