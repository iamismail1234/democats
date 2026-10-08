

with open("test.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("File handling in Python is easy.\n")

with open("test.txt", "r") as file:
    content = file.read()
    print(content)

with open("test.txt", "a") as file:
    file.write("Appending a new line to the file.\n")

with open("test.txt", "r") as file:
    content = file.read()
    print(content)

with open("test.txt", "r") as file:
    for line in file:
        print(line)

# readline() method reads a single line from the file. It returns an empty string when it reaches the end of the file.
with open("test.txt", "r") as file:
    print(file.readline())

#readlines() method reads all the lines from the file and returns them as a list of strings.
with open("test.txt", "r") as file:
    lines = file.readlines()
    print(lines)



    