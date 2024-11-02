
# Common Modes
# Mode	Description
# "r"	Read-only mode. Raises an error if the file does not exist.
# "w"	Write mode. Creates a new file or overwrites an existing file.
# "a"	Append mode. Adds content to the end of the file without overwriting it.
# "r+"	Read and write mode. Requires the file to already exist.
# "w+"	Write and read mode. Overwrites existing content or creates a new file.
# "a+"	Append and read mode. Adds content to the end and allows reading.


# reading from and writing to files
with open("example.txt", "w")as file:
    file.write("Hello, file!")
    
with open("example.txt","r") as file:
    content = file.read()
    print(content)
    
#exercise24hrs 
with open("name.txt", "w")as file:
    file.write("njeri, waweru, sospeter, wakaniaru, nyokabi, jared!")
    
with open("name.txt","r") as file:
    content = file.read()
    print(content)
    
# complex
# Write each name on a new line
with open("name.txt", "w") as file:
    names = ["njeri", "waweru", "sospeter", "wakaniaru", "nyokabi", "jared"]
    for name in names:
        file.write(name + "\n")

# Read the content back
with open("name.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())  # strip() removes extra newline characters
