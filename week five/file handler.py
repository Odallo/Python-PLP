# Creating and opening the file
with open("my_file.txt", 'w') as file:
    file.write("Hello, world!\n")
    file.write("The answer to the ultimate question of life, the universe, and everything is 42.\n")
    file.write("Goodbye, cruel world!\n")

# read file and print contents on the terminal
with open("my_file.txt", 'r') as file:
    contents = file.read()
    print(contents)

#appending to the file
with open("my_file.txt", "a") as file:
    file.write("This is an additional line of text.\n")
    file.write("This is the second line \n")
    file.write("this is the third line \n")

#erro handling
try:
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
        print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")
finally:
    print("File operation completed")