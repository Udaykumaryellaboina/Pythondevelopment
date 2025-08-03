

# 🎭 Abstraction in Python — Masterclass


'''## 🧠 **What is Abstraction?**

> **Abstraction** is the **process of hiding the implementation details**
 and **showing only essential features** of an object.

It is one of the **four pillars of OOP**:
**Encapsulation**, **Abstraction**, **Inheritance**, **Polymorphism**

---

### 🏁 Real-Life Analogy

**Car Driving:**

* You only need to know how to:

  * Start the car
  * Accelerate
  * Brake
* You **don’t need** to know:

  * How the engine works
  * How fuel is injected
  * Internal wiring

🎯 That’s **abstraction** – exposing **only what’s needed** and hiding everything else.

---

## 🔍 Abstraction vs Encapsulation

| Concept     | Abstraction                        | Encapsulation                  |
| ----------- | ---------------------------------- | ------------------------------ |
| Focus       | **Hides complexity**               | **Hides data**                 |
| Purpose     | Show **relevant behavior**         | Restrict **direct access**     |
| Achieved by | **Interfaces / Abstract classes**  | **Private/protected members**  |
| Example     | `car.start()` hides engine details | `__speed` attribute is private |

---

## 🔐 **Abstraction in Python**

Python supports abstraction via:

1. **Abstract Base Classes (`abc` module)**
2. **Interfaces (Pythonic version via ABCs)**
3. **Duck Typing (less strict, dynamic abstraction)**


## 🧰 1. **Using Abstract Base Class (`abc`)**

Python provides `abc` module to define abstract classes and methods.

### 🔸 Basic Structure
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

'''* `ABC` = Abstract Base Class
* `@abstractmethod` = Must be implemented by subclass
* Cannot instantiate `Animal` directly.'''


### 🧪 Full Example

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

d = Dog()
print(d.sound())  # Bark

### ⚠️ Instantiating Abstract Class

a = Animal()  # ❌ TypeError: Can't instantiate abstract class


## 🔁 Multiple Abstract Methods

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


## ✅ Concrete Methods in Abstract Class

#You can define both abstract and normal (concrete) methods.

class Machine(ABC):
    def power_on(self):
        print("Powering on...")

    @abstractmethod
    def operate(self):
        pass


'''## ⚙️ Interface-Like Behavior in Python

Python does **not have true interfaces** like Java or C#,
but we simulate interfaces via abstract classes **with only abstract methods**.
'''
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

#Any class inheriting `Shape` must implement all methods.



## 🦆 Duck Typing (Informal Abstraction)

#> “If it walks like a duck and quacks like a duck, it's a duck.”

#In Python, you can achieve abstraction without inheritance.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # No type checking

make_it_quack(Duck())
make_it_quack(Person())

#✅ This is **informal abstraction** via **dynamic typing**, but not enforced.


## 🚀 Real-World Example (FAANG Style)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ₹{amount} via Credit Card")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ₹{amount} via PayPal")

def process_payment(processor: PaymentProcessor, amount):
    processor.pay(amount)

process_payment(CreditCardProcessor(), 500)
process_payment(PayPalProcessor(), 1000)

'''### 💡 Benefits:

* `process_payment()` doesn’t care about **how** payment is made.
* Abstraction allows interchangeable processors.

## 🧠 Interview-Level Insights

### ✅ Common FAANG Interview Questions

#### Q1. How does abstraction help in scalable system design?

* Promotes separation of concerns
* Allows swappable components
* Encourages interface-driven development

#### Q2. How is abstraction implemented in Python without strict interfaces?

* Abstract base classes (`abc`)
* Duck typing
* Polymorphism

#### Q3. Can an abstract class have constructor?

* Yes, constructors (`__init__`) can be used in abstract classes.

---

## 🚫 Common Mistakes

| Mistake                             | Correction                                      |
| ----------------------------------- | ----------------------------------------------- |
| Instantiating abstract class        | Must inherit and implement all abstract methods |
| Forgetting to use `@abstractmethod` | Will allow instantiation                        |
| Overusing duck typing               | Prefer `abc` for stricter contracts             |

---

## 📋 Summary (Cheat Sheet)

| Concept                 | Explanation                               |
| ----------------------- | ----------------------------------------- |
| Abstraction             | Hide implementation, show interface       |
| Achieved by             | `abc.ABC`, `@abstractmethod`, duck typing |
| Benefit                 | Clean APIs, loose coupling, flexibility   |
| Python abstraction type | Abstract classes + duck typing            |
| Cannot do               | Instantiate abstract class directly       |'''

## 🧱 Bonus: Abstract Class with Constructor

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass

class FullTimeEmployee(Employee):
    def get_salary(self):
        return f"{self.name} gets ₹50,000/month"

print(FullTimeEmployee("Ravi").get_salary())
