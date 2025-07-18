'''List comprehension is a powerful and concise feature in Python for
creating new lists from existing iterables like lists, tuples, strings, sets, etc.,
using a single line of code. It makes code shorter, cleaner, and often more readable.'''

#✅ Basic Syntax of List Comprehension
'''[expression for item in iterable]
This is equivalent to:

result = []
for item in iterable:
    result.append(expression)'''

#🔹1. Simple List Comprehension
'Create a list of squares from 0 to 9:'

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#🔹2. List Comprehension with Condition (Filtering)
'Keep only even numbers:'

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


#🔹3. List Comprehension with if-else
'Add 1 if the number is even, else subtract 1:'

modified = [x + 1 if x % 2 == 0 else x - 1 for x in range(5)]
print(modified)  # Output: [1, 0, 3, 2, 5]

#❗ Note: When using if-else, it should be before for, unlike filtering which comes after.

#🔹4. Nested List Comprehension
'Creating a multiplication table:'

table = [[i * j for j in range(1, 6)] for i in range(1, 4)]
print(table)
# Output: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

#🔹5. Flatten a 2D List

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

#🔹6. Using Functions in List Comprehensions
def square(x):
    return x * x

results = [square(i) for i in range(5)]
print(results)  # Output: [0, 1, 4, 9, 16]

#🔹7. Using String List Comprehension
text = "hello"
uppercase = [char.upper() for char in text]
print(uppercase)  # Output: ['H', 'E', 'L', 'L', 'O']

#🔹8. With Multiple Conditions
nums = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(nums)  # Output: [0, 6, 12, 18]

#🔹9. With zip() Function
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired = [(name, score) for name, score in zip(names, scores)]
print(paired)
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

#🔹10. With enumerate() Function
lst = ["a", "b", "c"]
indexed = [(index, value) for index, value in enumerate(lst)]
print(indexed)  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]

#🔹11. Using List Comprehension with range()
'Create a list of all odd numbers from 1 to 20:'
odds = [x for x in range(1, 21) if x % 2 != 0]
print(odds)

#🔹12. Convert Nested Lists into Dictionary
data = [["a", 1], ["b", 2], ["c", 3]]
d = {k: v for k, v in data}
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}

#🔹13. Set and Dictionary Comprehension (Bonus)
# Set comprehension
squares_set = {x*x for x in range(5)}
print(squares_set)  # Output: {0, 1, 4, 9, 16}

# Dictionary comprehension
squares_dict = {x: x*x for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#💡 When to Use List Comprehensions
'''✅ When:

You want to create a new list from an existing iterable.
You want to filter or transform items in a clean and readable way.

❌ Avoid when:

The logic is too complex (deep nesting, many conditions).
Readability is more important than brevity.

✅ Summary Table
Concept	                           Syntax/Example
Basic	                     [x for x in iterable]
With condition	             [x for x in iterable if condition]
With if-else	             [x if cond else y for x in iterable]
Nested	                     [[x*y for y in Y] for x in X]
Flatten list	             [item for sublist in list for item in sublist]
With function	             [func(x) for x in iterable]
With multiple conditions	 [x for x in lst if cond1 if cond2]
With zip	                 [(a, b) for a, b in zip(A, B)]
With enumerate             	[(i, x) for i, x in enumerate(lst)]
Dict comprehension	         {k: v for k, v in pairs}
Set comprehension	         {x for x in iterable}'''


#🟢 Beginner Level Practice
'1. Create a list of squares from 1 to 10'
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [x**2 for x in range(1, 11)]

#2. Create a list of even numbers from 0 to 20
# Output: [0, 2, 4, ..., 20]
evens = [x for x in range(21) if x % 2 == 0]

#3. Convert a string to a list of its characters
# Input: "hello"
# Output: ['h', 'e', 'l', 'l', 'o']
chars = [ch for ch in "hello"]

#4. Convert all words in a list to uppercase
words = ['python', 'list', 'comprehension']
uppercase = [word.upper() for word in words]

#🟡 Intermediate Level Practice
#5. Replace even numbers with "even" and odd with "odd" for 1 to 10
labels = ['even' if x % 2 == 0 else 'odd' for x in range(1, 11)]
# Output: ['odd', 'even', 'odd', 'even', ..., 'even']

#6. Create a list of tuples (x, x²) for x from 1 to 5
pairs = [(x, x**2) for x in range(1, 6)]
# Output: [(1,1), (2,4), (3,9), (4,16), (5,25)]

#7. Filter names starting with 'A'
names = ['Alice', 'Bob', 'Angela', 'Charlie']
filtered = [name for name in names if name.startswith('A')]

#8. Flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
#9. Get only digits from a string
s = "abc123xyz"
digits = [ch for ch in s if ch.isdigit()]
# Output: ['1', '2', '3']

#10. List of ASCII codes of vowels
vowels = "aeiou"
ascii_codes = [ord(ch) for ch in vowels]
# Output: [97, 101, 105, 111, 117]

#🔴 Advanced / Interview-Level Questions
#11. Transpose a matrix using list comprehension
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Output: [[1, 4], [2, 5], [3, 6]]

#12. Remove duplicates from a list using list comprehension
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
[unique.append(x) for x in nums if x not in unique]
# Output: [1, 2, 3, 4, 5]

#13. Nested conditional comprehension
nums = [10, 15, 20, 25, 30]
labels = ["div by 10" if x % 10 == 0 else "not div by 10" for x in nums]

#14. Build a dictionary of word lengths
words = ['python', 'java', 'cpp']
length_dict = {word: len(word) for word in words}
# Output: {'python': 6, 'java': 4, 'cpp': 3}

#15. Find all prime numbers from 1 to 50 using list comprehension
primes = [x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]