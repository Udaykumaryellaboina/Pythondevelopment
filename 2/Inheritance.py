# 🧬 Inheritance in Python — The Complete Guide

## 🧠 **What is Inheritance?**
''' **Inheritance** is an **OOP feature** where one class (**child/derived**)
 **inherits the properties and behaviors** (attributes and methods) of another class (**parent/base**).

🔹 Helps in **code reuse**
🔹 Enables **polymorphism**
🔹 Encourages **DRY** (Don't Repeat Yourself) principle
🔹 Allows **extensibility**


## ⚙️ **Basic Syntax**'''

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()  # Output: Hello from Parent

#✅ The child class `Child` inherited the `greet()` method from `Parent`.


## 🔍 **Why Use Inheritance?**

'''| Benefit         | Description                                           |
| --------------- | ----------------------------------------------------- |
| ✅ Reusability   | Common logic in base class, reused in derived classes |
| ✅ Extensibility | Easily add/override functionality                     |
| ✅ Polymorphism  | Interface behaves differently based on object         |
| ✅ Organization  | Clear hierarchy and relationships                     |



## 🔠 **Types of Inheritance in Python**

Python supports **5 types** of inheritance:

| Type                     | Example                        |
| ------------------------ | ------------------------------ |
| Single Inheritance       | One child, one parent          |
| Multilevel Inheritance   | Chain: A → B → C               |
| Hierarchical Inheritance | One parent → multiple children |
| Multiple Inheritance     | One child ← multiple parents   |
| Hybrid Inheritance       | Combination of above           |

### 📌 1. **Single Inheritance**'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # from parent
d.bark()   # from child

### 📌 2. **Multilevel Inheritance**

class Grandparent:
    def feature1(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def feature2(self):
        print("Feature from Parent")

class Child(Parent):
    def feature3(self):
        print("Feature from Child")

c = Child()
c.feature1()
c.feature2()
c.feature3()


### 📌 3. **Hierarchical Inheritance**

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

car = Car()
car.start()
bike = Bike()
bike.start()


### 📌 4. **Multiple Inheritance**

class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def skill(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()  # Output: Gardening (MRO: Left to right)
'''
> 🧠 **Method Resolution Order (MRO)**: Python follows **C3 Linearization 
(left-to-right depth-first)** in resolving multiple inheritance.

Use `ClassName.__mro__` or `help(ClassName)` to inspect.



### 📌 5. **Hybrid Inheritance**'''
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):  # Combines multiple and multilevel
    pass


## 🛠️ **Constructor in Inheritance (`__init__`)**

### 🔹 Calling Parent Constructor

class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()  # call parent constructor
        print("B constructor")

b = B()

#> ✅ `super()` is used to access parent methods/constructors **especially in multiple inheritance**.

## ⚔️ **Method Overriding**

#> Child class can **override** a method of the parent.

class Parent:
    def show(self):
        print("Parent show")

class Child(Parent):
    def show(self):  # overridden
        print("Child show")

c = Child()
c.show()


'''## 🧬 **super() vs direct class name**

| `super()`                           | `Parent.method(self)`  |
| ----------------------------------- | ---------------------- |
| Follows MRO                         | Doesn't follow MRO     |
| Used in multiple inheritance safely | May break MRO          |
| Preferred in Python                 | Legacy or explicit use |



## 💡 Real-World Example

```python'''
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

acc = SavingsAccount(1000, 0.05)
acc.add_interest()
print(acc.get_balance())  # 1050.0


'''## 🧪 Interview-Level Questions (FAANG)

### Q1. What is Method Resolution Order (MRO) and how does Python handle it?

> Python uses **C3 Linearization**. You can view MRO via `Class.__mro__`.

### Q2. How does `super()` work in multiple inheritance?

> It calls the **next method in MRO**, ensuring correct method resolution and avoiding redundancy.

### Q3. Can `super()` skip intermediate classes?

> No. It strictly follows the MRO sequence.

### Q4. What’s the difference between `is-a` and `has-a` relationship?

* **Inheritance** models `is-a` (e.g., `Dog is-a Animal`)
* **Composition** models `has-a` (e.g., `Car has-a Engine`)

### Q5. When should you not use inheritance?

* When behavior is not truly shared
* When **composition** is a better fit
* When you need flexibility, not tight coupling

---

## ❗ Common Pitfalls

| Mistake                                 | Fix                                        |
| --------------------------------------- | ------------------------------------------ |
| Forgetting to call `super().__init__()` | Always call base constructor if overriding |
| Accessing private members from subclass | Use protected instead                      |
| Misusing multiple inheritance           | Understand MRO first                       |

---

## 🧾 Summary Cheatsheet

| Concept        | Key Point                                          |
| -------------- | -------------------------------------------------- |
| Inheritance    | Reuse logic across classes                         |
| `super()`      | Calls parent class methods                         |
| MRO            | Method resolution in multiple inheritance          |
| Overriding     | Redefine base class methods                        |
| Types          | Single, Multilevel, Hierarchical, Multiple, Hybrid |
| Python Feature | Dynamic, flexible, supports all types              |

---'''

