#✅ What is a dict in Python?

"""A dictionary is:

A collection of key-value pairs

Unordered in versions < 3.7, but insertion-ordered in Python 3.7+

Mutable (can add, update, delete entries)

Keys must be unique and hashable

Values can be of any data type

🔹 Example"""

person = {"name": "Alice", "age": 30, "is_student": False}
'''

🧠 Key Features
Property	            Example	                              Explanation
Keys must be unique	    {"a": 1, "a": 2} → {"a": 2}	          Last value overwrites earlier
Keys must be hashable	dict({[1,2]: "list"})                 ❌ Error	Lists can't be keys
Access by key	        person["name"] → "Alice"	           Direct lookup
Mutable	                person["age"] = 31	                   You can change values
'''

'''
🧰 Built-in Dictionary Methods

Method	                       Description	                                                    Example
get(key[, default])        	Return value of key, return default if not found	                d.get("x", 0)
keys()	                    Return view of all keys	                                            d.keys()
values()	                Return view of all values	                                        d.values()
items()	                    Return view of (key, value) pairs	                                d.items()
update(dict2)	            Add/update entries from another dictionary	                        d.update({"x": 1})
pop(key[, default])       	Remove specified key and return value	                            d.pop("x", "Not Found")
popitem()	                Remove and return the last inserted (key, value) pair	            d.popitem()
clear()	                    Remove all items	                                                d.clear()
copy()	                    Return a shallow copy	                                            d2 = d.copy()
setdefault(k[, v])	        Get value of k, insert if not found	                               d.setdefault("z", 100)
fromkeys(iterable, value)	Create new dict with keys from iterable & same value	           dict.fromkeys(["a", "b"], 0)

📌 Example Code
'''
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])           # Alice
print(person.get("gender", "N/A"))  # N/A

person["age"] = 26
person["gender"] = "Female"

print(person.keys())            # dict_keys(['name', 'age', 'city', 'gender'])
print(person.values())          # dict_values(['Alice', 26, 'New York', 'Female'])

person.pop("city")              # Removes 'city'
print(person)

person.update({"job": "Engineer"})
print(person)

d2 = person.copy()
print(d2)

person.clear()
print(person)  # {}

#🔄 Dictionary Comprehension

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#🔒 Immutable Keys Only
#Valid keys:


{"a": 1, 10: "x", (1, 2): "tuple"}

#Invalid key:

{[1, 2]: "list"}  # ❌ TypeError: unhashable type: 'list'


#🧠 FAANG Tip:
#Use .get() and .setdefault() for safe lookups and default initialization in loops:


d = {}
for ch in "banana":
    d[ch] = d.get(ch, 0) + 1
print(d)  # {'b': 1, 'a': 3, 'n': 2}


