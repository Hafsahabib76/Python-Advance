# Creates a new text file called "my_file.txt"
file = open("my_file.txt", "w")

# Writes the following lines
file.write(f"Hello, this is my first file handling assignment. \nI am learning Python file operations.")

file.close()

# Create a function read_file(filename) that takes a filename as a parameter
# and reads and displays the content of the file.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# Test this function by passing "my_file.txt" as an argument.
read_file("my_file.txt")

# # Write a function append_to_file(filename, text) that takes a filename and a string as parameters
# # and appends the string to the existing file.
def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(f"\n{text}")


append_to_file("my_file.txt", "This is additional content")