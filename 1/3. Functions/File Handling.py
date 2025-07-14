'''File handling in Python allows you to create, read, write, append, and
delete files using built-in functions. Python uses the open() function
for file operations and provides several methods to handle file input/output.'''

#🔷 File Handling Basics

'''Open the file using open()

Read/Write the file using methods like read(), write()

Close the file using close() (or use a with block)
'''

#🔹 1. open() Function
#📌 Syntax:

file = open("filename", "mode")

'''📘 Modes:
Mode	Description
'r'	    Read (default). Error if file not found
'w'	    Write. Creates file if not exists, overwrites if it does
'a'  	Append. Creates file if not exists, adds to the end
'x'	    Create. Fails if file already exists
'b'	    Binary mode (e.g., rb, wb)
't'	    Text mode (default, e.g., rt, wt)'''

#🔹 2. Reading from a File
'''✅ Methods:
Method	    Description
read()	    Reads the entire file
read(n)	    Reads first n characters
readline()	Reads one line at a time
readlines()	Reads all lines into a list
'''
#✅ Example:

f = open("sample.txt", "r")
print(f.read())         # Reads entire file
f.close()

#🔹 3. Writing to a File
#✅ write() Method:

f = open("sample.txt", "w")
f.write("Hello, world!")
f.close()

#Note: 'w' mode overwrites the content if the file exists.

#🔹 4. Appending to a File
#✅ append() Mode:

f = open("sample.txt", "a")
f.write("\nAppended line.")
f.close()

#🔹 5. Using with Statement (Best Practice)
#Automatically handles closing the file.

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

#✅ No need to call f.close().

##✅ Writing multiple lines:

lines = ["Line 1\n", "Line 2\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)

#✅ Reading as list:

with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n']

#🔹 7. File Object Methods

'''Method	          Description
read()	          Read full content
readline()	      Read one line
readlines()	      Read all lines as a list
write(str)	      Write a string to file
writelines()	  Write a list of strings to file
seek(offset)	  Move file pointer to offset
tell()	          Returns the current position of pointer
close()           Close the file
flush()        	  Force write buffer to file'''

#🔹 8. File Pointer Control: seek() and tell()

with open("file.txt", "r") as f:
    print(f.tell())     # Position: 0
    f.read(5)
    print(f.tell())     # Position: 5
    f.seek(0)           # Back to start

#🔹 9. Checking and Deleting Files
#Use the os module:

import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist.")

#🔚 Summary
'''
Function / Method	Description
open()	            Open a file
read()	            Read whole file
readline()	        Read one line
write()	            Write to file
writelines()	    Write multiple lines
close()	            Close the file
with	            Context manager (auto-close)
seek()	            Move file pointer
tell()	            Get current file pointer
os.remove()	        Delete a file'''

