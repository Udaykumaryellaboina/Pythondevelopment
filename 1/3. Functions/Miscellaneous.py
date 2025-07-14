#🔷 1. help() – Access Built-in Documentation
'''✅ Purpose:
Displays the documentation/help of objects like modules, functions, classes, etc.

✅ Syntax:
help(object)
✅ Examples:'''

help(len)          # Shows help about len() function
help(str)          # Shows all methods in str class

#You can also use it interactively in the Python shell:


#>>> help()
#Help on help command
#🧠 Very useful for beginners to explore the built-in functionality.

#🔷 2. dir() – List Attributes and Methods
#✅ Purpose:
'''Returns a list of names in the current scope or inside an object (functions, variables, methods, etc.)

✅ Syntax:
dir([object])
✅ Examples:'''

print(dir())           # Shows current scope's variable names
print(dir(str))        # Shows all string methods
print(dir([]))         # Shows list methods

#Useful to explore what methods/attributes an object has.

#🔷 3. locals() – Dictionary of Local Scope
'''✅ Purpose:
Returns a dictionary of all local variables in the current function/scope.
✅ Syntax:
locals()
✅ Example:'''
def demo():
    x = 10
    y = 20
    print(locals())

demo()
# Output: {'x': 10, 'y': 20}
#🔷 4. globals() – Dictionary of Global Scope
'''✅ Purpose:
Returns a dictionary of all global variables and functions.
✅ Syntax:
globals()
✅ Example:'''

x = 5
def show_globals():
    print(globals()['x'])  # Access global variable

show_globals()
'''Both locals() and globals() return modifiable dictionaries,
but modifying them directly is not recommended in most cases.'''

#🔷 5. callable() – Check If an Object Is Callable
'''✅ Purpose:
Checks if an object can be called like a function (i.e., if it implements the __call__() method).
✅ Syntax:
callable(object)
✅ Examples:
'''
def foo():
    pass

print(callable(foo))      # True

x = 10
print(callable(x))        # False

#✅ Works on classes and methods:
class A:
    def __call__(self):
        print("Called!")

a = A()
print(callable(a))  # True

#✅ Summary Table
'''Function	Description
help(obj)	Shows documentation of a module/function/class
dir(obj)	Lists attributes and methods of an object or current scope
locals()	Returns local symbol table (dict of local variables)
globals()	Returns global symbol table (dict of global variables)
callable()	Checks if an object is callable (like a function/class)'''

#✅ Real-World Use Case

def explore(obj):
    if callable(obj):
        print(f"{obj} is callable")
    else:
        print(f"{obj} is NOT callable")
    print("Available methods:", dir(obj))
    print("Documentation:")
    help(obj)
