# 🐍 Python Classes – Beginner to Advanced Concepts
## 📌 What is a Class?

'''
A **class** is a blueprint for creating **objects**. Objects are instances of classes that contain
**attributes (variables)** and **methods (functions)**.

> Think of a **class** as a blueprint of a "Car" – it defines properties like color, brand, and
methods like drive or brake. A real car (like your Honda Civic) is an **object** based on that class.

'''

## ✅ Why Use Classes?
'''
* Organize code using **Object-Oriented Programming (OOP)**
* Reuse code via **inheritance**
* Represent real-world entities in a cleaner way

'''

## 🧱 Class Syntax

class ClassName:
    # constructor (called when object is created)
    def __init__(self, param1, param2):
        self.param1 = param1  # instance variable
        self.param2 = param2

    # method
    def show_info(self):
        print(f"Param1: {self.param1}, Param2: {self.param2}")

### 🎯 Example:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

## 🎬 Creating Objects


# Create an object of Person class
p1 = Person("Alice", 30)
p1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
# Create another object
p2 = Person("Bob", 25)
p2.greet()  # Output: Hello, my name is Bob and I am 25 years old.      


## 🔍 Key Concepts

### 1. **`__init__()` Constructor**

#Automatically called when an object is created.


def __init__(self, name):
    self.name = name


### 2. **`self`**

#Refers to the **current object instance**. Needed to access variables and methods.

self.name = name  # Assigning to the object’s name variable

### 3. **Instance Variables vs Class Variables**

'''* **Instance Variable**: Belongs to object
* **Class Variable**: Shared across all objects
'''

class Dog:
    species = "Canis"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

'''Great! Let’s go deeper into **Python Classes** and explore all important advanced
and intermediate concepts **step by step**, in a way that's easy to follow.

'''

# 🧠 Python Classes – Intermediate to Advanced Concepts

## 📌 1. Class vs Object

'''A **class** is a blueprint for creating objects. An **object** is an instance of a class.
| Term       | Meaning                |
| ---------- | ---------------------- |
| **Class**  | A blueprint            |
| **Object** | An instance of a class |'''


class Fruit:
    pass

apple = Fruit()  # apple is an object of class Fruit

banana = Fruit()  # banana is another object of class Fruit
## 📌 2. Instance Methods, Class Methods, Static Methods

### ✅ Instance Method

#Works with object (`self`)

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I’m {self.name}")

### ✅ Class Method

#Works with class (`cls`), not instance

class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school

### ✅ Static Method

#No `self` or `cls`, utility method

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(2, 3))  # 5

## 📌 3. `__str__()` and `__repr__()` – Object Representation
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)  # Calls __str__


## 📌 4. Inheritance Deep Dive

### 👉 Single Inheritance

class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

### 👉 Multilevel Inheritance

class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass
### 👉 Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
### 👉 Single Inheritance with Method Overriding
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
d = Dog()
d.speak()  # Bark
### 👉 Super() Function
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Animal's speak
        print("Bark")
### 👉 Multiple Inheritance

class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Art, Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Father’s skills method due to MRO


## 📌 5. Method Resolution Order (MRO)

'''Python follows **left-to-right** in multiple inheritance.

Use `ClassName.__mro__` or `help(ClassName)` to check it.
'''
## 📌 6. Private, Protected and Public Members

### ✅ Public: Accessible everywhere

self.name = "Alice"

### ✅ Protected: Use single underscore

self._salary = 50000

### ✅ Private: Use double underscore

self.__bank_balance = 100000

#Access private:

print(obj._ClassName__bank_balance)


## 📌 7. Property Decorator – Getter & Setter

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Invalid salary")
        self._salary = value


## 📌 8. Abstract Class & Method – `abc` Module

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

#* Cannot instantiate `Shape` directly.


## 📌 9. Polymorphism

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())


## 📌 10. Composition vs Inheritance

'''* **Inheritance**: “Is-A” relationship
* **Composition**: “Has-A” relationship
'''
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # has-a relationship

    def drive(self):
        self.engine.start()
        print("Car is moving")


## 📌 11. Class Attributes vs Instance Attributes

class Demo:
    class_var = 10  # shared

    def __init__(self):
        self.instance_var = 20  # per object


## 📌 12. Magic / Dunder Methods (`__add__`, `__len__`, etc.)

### `__len__`

class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

ml = MyList([1, 2, 3])
print(len(ml))  # 3

### `__add__`

class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)


## 🧪 Mini Project – Bank Account

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

a1 = BankAccount("Uday", 1000)
a1.deposit(500)
print(a1.get_balance())  # 1500


