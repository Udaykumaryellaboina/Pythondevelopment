## 🔒 **What is Encapsulation?**


'''**Encapsulation** is the **bundling of data (variables)** and **methods (functions)** that
operate on that data into a **single unit (class)**, and **restricting direct access** to 
some of the object's components.

This means:

* Internal object state can be **hidden** from the outside.
* Access is **controlled** using **public**, **protected**, or **private** access modifiers.



## 🧱 **Why Encapsulation?**

Encapsulation ensures:

* ✅ Data hiding & abstraction
* ✅ Better modularity
* ✅ Loose coupling (objects interact via interfaces, not internals)
* ✅ Better maintainability and debugging
* ✅ Security: Prevents unintended access/modification


## 🧠 **How is Encapsulation Implemented in Python?**

Python doesn’t have keywords like `public`, `private`, or `protected`, but it uses:

* **Naming conventions** and
* **Name mangling**

### Access Modifiers in Python (Convention-Based):

| Modifier  | Syntax       | Access Level                                        |
| --------- | ------------ | --------------------------------------------------- |
| Public    | `variable`   | Accessible from anywhere                            |
| Protected | `_variable`  | Accessible inside class & subclasses                |
| Private   | `__variable` | Not accessible directly from outside (name mangled) |



## 🔎 **1. Public Members**

'''
class Employee:
    def __init__(self, name):
        self.name = name  # public

e = Employee("Alice")
print(e.name)  # ✅ Accessible


## 🛡 **2. Protected Members** (convention only)

class Employee:
    def __init__(self, name):
        self._name = name  # protected

class Manager(Employee):
    def get_name(self):
        return self._name  # ✅ Accessible in subclass

m = Manager("Bob")
print(m.get_name())      # ✅
print(m._name)           # ⚠️ Not recommended

## 🔐 **3. Private Members (Name Mangling)**

class Employee:
    def __init__(self, name):
        self.__name = name  # private

    def get_name(self):
        return self.__name  # access via method

e = Employee("Charlie")
print(e.get_name())      # ✅

print(e.__name)          # ❌ AttributeError
print(e._Employee__name) # ✅ Not recommended (name mangling)

#> 🧠 Name mangling makes `__name` → `_Employee__name` behind the scenes.


## 🔄 **Getters and Setters in Python**

#Encapsulation usually involves **controlling access** via **getters and setters**.

class Account:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

acc = Account()
acc.set_balance(1000)     # ✅
print(acc.get_balance())  # 1000


## 🎯 Pythonic Way: Using `@property` Decorator
class Product:
  
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

p = Product()
p.price = 200      # ✅ uses setter
print(p.price)     # ✅ uses getter

## 📝 Summary
# **Encapsulation** is the bundling of data and methods that operate on that data within a single unit (class).
# It restricts direct access to some components, promoting data hiding and abstraction.
# Implemented in Python using naming conventions and name mangling.
# Benefits include improved modularity, maintainability, and security.      
#> Encapsulation is a fundamental principle of Object-Oriented Programming (OOP) that helps in building robust and maintainable code.
#> It allows you to control how data is accessed and modified, ensuring that the internal state of an object is protected from unintended interference.
#> This leads to cleaner, more understandable code and reduces the risk of bugs.    

#> Encapsulation is a key concept in OOP that enhances code organization and security.
#> It allows you to bundle data and methods together, controlling access to the internal state of objects.
#> By using encapsulation, you can create classes that are easier to maintain and debug,

#> while also ensuring that the data remains consistent and secure.

#> Encapsulation is a powerful tool in Python that helps you write cleaner, more maintainable code.
#> It allows you to define clear interfaces for your classes, ensuring that the internal state is   
#> protected and that data is accessed in a controlled manner.
#> By using encapsulation, you can create robust applications that are easier to understand and modify
#> over time.
