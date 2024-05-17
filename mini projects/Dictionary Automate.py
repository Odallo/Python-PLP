import json
from difflib import get_close_matches

# Load dictionary data from JSON file
with open('dictionary (1).json') as f:
    data = json.load(f)

# Function to get definition of a word
def get_definition(word):
    word = word.lower()  # Convert word to lowercase
    if word in data:
        return data[word]
    else:
        matches = get_close_matches(word, data.keys(), n=1)
        if matches:
            suggestion = matches[0]
            confirm = input(f"Did you mean '{suggestion}' instead of '{word}'? Enter 'y' for yes, 'n' for no: ")
            if confirm.lower() == 'y':
                return data[suggestion]
        return "Word not found in dictionary."

# Main program loop
while True:
    search_word = input("Enter a word to search for its definition (type 'q' to quit): ")
    if search_word.lower() == 'q':
        break
    definition = get_definition(search_word)
    print(definition)

