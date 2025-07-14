
#🔷 1. input() Function – For Taking Input from the User
#✅ Syntax:

variable = input("Prompt message")
'''It always returns the input as a string (str type).

You can convert the input to other types like int, float, etc.

✅ Example:'''

name = input("Enter your name: ")
print("Hello,", name)

age = int(input("Enter your age: "))
print("Next year, you'll be", age + 1)
#🧠 Tip: Always convert input to the correct data type if needed.

#🔷 2. print() Function – For Displaying Output
#✅ Syntax:

#print(object(s), sep=' ', end='\n', file=sys.stdout, flush=False)

#🔹 Common Parameters:
'''Parameter	Description
sep	        Separator between multiple items (default is space ' ')
end	        What to print at the end (default is newline \n)
file	    Where to send output (default is screen / stdout)
flush	    If True, forces the output to be written immediately

✅ Examples:'''

print("Hello, world!")
#Print multiple values:

print("Python", "is", "fun")  # Output: Python is fun

#Change separator:

print("2025", "07", "14", sep="-")  # Output: 2025-07-14
#Change end character:

print("Hello", end=" ")
print("World")  # Output: Hello World

#Print to a file:

with open("output.txt", "w") as f:
    print("Writing to file", file=f)

#🔷 3. String Formatting for Output
#✅ 1. Using + operator:

name = "Alice"
print("Hello " + name)
#✅ 2. Using , in print() (auto spacing):

age = 25
print("Age is", age)

#✅ 3. Using f-strings (modern and recommended):

name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

#✅ 4. Using format() method:

print("My name is {} and I am {} years old.".format("Alice", 25))

#🔷 4. Advanced Input Techniques
#You can take multiple values in a single line:

x, y = input("Enter two numbers: ").split()
print("x =", x, ", y =", y)
#With type casting:

a, b = map(int, input("Enter two integers: ").split())
print(a + b)

'''✅ Summary Table
Function	Purpose                 	            Example
input()	    Takes user input (as a string)	        name = input("Enter name: ")
print()  	Displays output to screen	            print("Hello")
f-string	Format output (since Python 3.6)	    print(f"Age: {age}")
format()	Old-style formatting	               "{} is {}".format("Age", 25)
sep	Change separator in print	                    print("A", "B", sep="-")
end	Change line ending	                            print("Hello", end="!")'''