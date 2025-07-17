#📌 What is File Handling?
'''File handling allows us to read from and
write to files stored on disk using Python. It's essential for:

Reading data from files
Writing logs or reports
Saving program output

🔹 Built-in open() Function
Syntax:
 = open("filename", "mode")
Modes of Opening Files:
Mode	Meaning
'r'	Read (default). Error if file doesn’t exist
'w'	Write. Creates file if not exists, overwrites if exists
'a'	Append. Creates file if not exists, adds data to end
'x'	Create new file. Error if file exists
'b'	Binary mode (e.g. 'rb', 'wb')
't'	Text mode (default)
'+'	Read and write both ('r+', 'w+', 'a+')

✅ Examples
1. Reading from a File'''
from semver import process

f = open("sample.txt", "r")
content = f.read()
print(content)
f.close()

#🔸 read() reads entire file as a string.

#2. Reading Line by Line

f = open("sample.txt", "r")
for line in f:
    print(line.strip())
f.close()

#OR

lines = f.readlines()  # Returns a list of lines

#3. Writing to a File

f = open("output.txt", "w")
f.write("Hello, World!\n")
f.write("Python File Handling")
f.close()

#🔸 Overwrites the file if it already exists.

#4. Appending to a File
f = open("output.txt", "a")
f.write("\nThis is an added line.")
f.close()

#🔹 Using with Statement (Best Practice)
#Automatically closes the file after block execution.

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
#🔹 Reading File in Different Ways
f.read()          # Entire content
f.readline()      # Reads one line
f.readlines()     # List of all lines

#🔹 Writing Binary Files
with open("image.jpg", "rb") as f:
    binary_data = f.read()
with open("copy.jpg", "wb") as f:
    f.write(binary_data)

#🔹 File Methods
'''Method	           Description
read(size)	       Reads specified size in bytes
readline()	       Reads one line
readlines()	        Reads all lines
write(str)	        Writes a string
writelines(list)	Writes list of strings
seek(offset)	    Moves cursor to a specific position
tell()	            Returns current cursor position
close()	            Closes the file
'''

#🔸 seek() and tell() Example

f = open("sample.txt", "r")
print(f.tell())         # 0
print(f.read(5))        # Read 5 chars
print(f.tell())         # 5
f.seek(0)               # Go back to start
print(f.read(5))        # Read first 5 again
f.close()


#🔹 Checking If File Exists
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist")
#🔹 Delete a File
import os

os.remove("sample.txt")

#🔹 Create New Directory and File
os.mkdir("new_folder")  # Create folder

with open("new_folder/notes.txt", "w") as f:
    f.write("Hello")

#🔹 Rename or Move File
os.rename("old.txt", "new.txt")

#🔹 Exception Handling with Files
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

#🔹 Reading Large Files Efficiently
with open("largefile.txt", "r") as f:
    for line in f:
        process(line)  # line-by-line, low memory usage

#🔹 writelines() Example

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)
#🔹 File Pointer Positions (using seek)
f = open("test.txt", "r")
print(f.tell())   # Show pointer (e.g., 0)
f.seek(5)         # Move to 5th byte
print(f.read())   # Read from 6th character
f.close()

#🔹 Working with CSV Files (Bonus)
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
''''🔹
Summary Table
Task	                 Code
Open file	             open("file.txt", "r")
Close file	             f.close()
Read full content	     f.read()
Read one line	         f.readline()
Read all lines	         f.readlines()
Write to file	         f.write("text")
Append to file	         open("file.txt", "a")
Best practice	         with open(...) as f:
Check exists	         os.path.exists()
Delete	                 os.remove()
Seek position           	f.seek(pos)
Get position	         f.tell()'''

