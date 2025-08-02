

#* Objects in Python
#* Objects are instances of classes that encapsulate data and behavior.
#* They allow for data encapsulation, abstraction, and code reuse.  
#* Objects can be created from classes, and each object can have its own state and behavior.
#* Objects are fundamental to Object-Oriented Programming (OOP) in Python.
#* They can be created, modified, and interacted with using methods defined in their class.
#* Objects can also have attributes and methods that define their properties and behaviors.
#* Objects can be created dynamically, allowing for flexible and reusable code.
#* Objects can be used to represent real-world entities, making code more intuitive and organized.
#* Objects can be passed as arguments to functions, returned from functions, and stored in data structures.
#* Objects can be compared, copied, and manipulated using various built-in methods.
#* Objects can be serialized and deserialized, allowing for data persistence.
#* Objects can be used in various design patterns, such as Singleton, Factory, and Observer



# 🧱 What Are Objects in Python?

## 🧠 **Definition:**

'''An **object** is an **instance of a class**. It is a real-world entity created 
based on the **blueprint defined in the class**.

> Think of a **class** as a "recipe" and an **object** as the "cake" made using that recipe.
'''

## 📌 Why Are Objects Important?

'''* They **hold data** (attributes)
* They **perform actions** (methods)
* They are the **building blocks of Object-Oriented Programming (OOP)**
'''

## ✅ Example

### Step 1: Define a Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

### Step 2: Create an Object

p1 = Person("Alice", 30)  # p1 is an object

### Step 3: Use the Object

print(p1.name)     # Output: Alice
print(p1.age)      # Output: 30
p1.greet()         # Output: Hello, my name is Alice.


## 📦 Object = Data + Behavior

'''| Element      | In Code       |
| ------------ | ------------- |
| **Data**     | `name`, `age` |
| **Behavior** | `greet()`     |

'''

## 🧬 How Objects Are Created Internally

p1 = Person("Alice", 30)
'''When you create an object like `p1`, Python does the following:
1. Allocates memory for the object
2. Calls `__init__()` to initialize `name` and `age`
3. Assigns methods like `greet()` to that object
'''

## 📍 Object Identity and Type

print(type(p1))        # <class '__main__.Person'>
print(id(p1))          # Memory address (e.g., 140736830)


## 🛠 Accessing and Modifying Object Properties

p1.name = "Bob"
print(p1.name)  # Bob
# You can also access methods
p1.greet()  # Output: Hello, my name is Bob.
## 🏷 Adding New Attributes Dynamically

p1.city = "New York"
print(p1.city)  # New York
# You can add new attributes to an object at runtime
p1.country = "USA"
print(p1.country)  # USA
# Objects can be modified dynamically, allowing for flexible data structures.
## 🧩 Object Lifecycle

'''1. **Creation**: When an object is created, memory is allocated, and the `__init__` method is called.
2. **Usage**: The object can be used by accessing its attributes and methods.
3. **Modification**: Attributes can be added, modified, or deleted at runtime.
4. **Destruction**: When an object is no longer needed, it can be deleted using `del`, and memory is freed.'''
## 🧪 Practice Example
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model  

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")
acc = BankAccount(1000) 
print(acc.get_balance())         # 1000
# print(acc.__balance)  # Error!


## 🔁 Multiple Objects from Same Class

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

p1.greet()  # Alice
p2.greet()  # Bob
# Each object has its own state and behavior.
#Each object has its **own copy** of variables (`name`, `age`).

## 💡 Key Notes
'''

| Term         | Meaning                                    |
| ------------ | ------------------------------------------ |
| `object`     | An instance of a class                     |
| `attributes` | Variables inside the object (`self.name`)  |
| `methods`    | Functions defined in class (`def greet()`) |
| `__init__()` | Constructor to initialize object           |
| `self`       | Refers to the current object               |

'''

## 🧪 Practice Example

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB")

l1 = Laptop("Dell", 16)
l2 = Laptop("HP", 8)

l1.show_specs()  # Brand: Dell, RAM: 16GB
l2.show_specs()  # Brand: HP, RAM: 8GB



#* Objects are instances of classes that encapsulate data and behavior.
#* They allow for data encapsulation, abstraction, and code reuse.
#* Objects can be created from classes, and each object can have its own state and behavior.
#* Objects are fundamental to Object-Oriented Programming (OOP) in Python.
#* They can be created, modified, and interacted with using methods defined in their class.
#* Objects can also have attributes and methods that define their properties and behaviors.

#* Objects can be created dynamically, allowing for flexible and reusable code.
#* Objects can be used to represent real-world entities, making code more intuitive and organized.
#* Objects can be passed as arguments to functions, returned from functions, and stored in data structures.
#* Objects can be compared, copied, and manipulated using various built-in methods.
#* Objects can be serialized and deserialized, allowing for data persistence.
#* Objects can be used in various design patterns, such as Singleton, Factory, and Observer.
#* Objects can be used to implement polymorphism, allowing for different behaviors based on the object type.
#* Objects can be used to implement encapsulation, hiding internal state and exposing only necessary methods.
#* Objects can be used to implement inheritance, allowing for code reuse and extension of existing classes.
#* Objects can be used to implement composition, allowing for complex behaviors by combining simple objects.
#* Objects can be used to implement interfaces, allowing for a common contract between different classes.
#* Objects can be used to implement decorators, allowing for dynamic behavior modification.
#* Objects can be used to implement metaclasses, allowing for class-level customization.
#* Objects can be used to implement context managers, allowing for resource management.
#* Objects can be used to implement iterators, allowing for custom iteration behavior.
#* Objects can be used to implement generators, allowing for lazy evaluation of sequences.
#* Objects can be used to implement coroutines, allowing for asynchronous programming.
#* Objects can be used to implement data classes, allowing for easy creation of classes with attributes.
#* Objects can be used to implement named tuples, allowing for immutable data structures.
#* Objects can be used to implement slots, allowing for memory-efficient attribute storage.
#* Objects can be used to implement properties, allowing for controlled access to attributes.
#* Objects can be used to implement class methods and static methods, allowing for alternative ways to define methods.
#* Objects can be used to implement class variables, allowing for shared state across instances.
#* Objects can be used to implement class inheritance, allowing for code reuse and extension of existing classes.
#* Objects can be used to implement multiple inheritance, allowing for complex class hierarchies.
#* Objects can be used to implement abstract base classes, allowing for a common interface across different classes.
#* Objects can be used to implement mixins, allowing for reusable behavior across different classes.
#* Objects can be used to implement class decorators, allowing for dynamic class modification.
#* Objects can be used to implement class factories, allowing for dynamic class creation.
#* Objects can be used to implement class registries, allowing for dynamic class discovery.

#* Objects can be used to implement class serialization, allowing for data persistence.
#* Objects can be used to implement class deserialization, allowing for data retrieval.
#* Objects can be used to implement class introspection, allowing for dynamic class inspection.
#* Objects can be used to implement class reflection, allowing for dynamic class modification.
#* Objects can be used to implement class validation, allowing for data integrity checks.