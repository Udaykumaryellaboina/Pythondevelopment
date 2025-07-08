#🔵 What is a for loop?
'''A for loop in Python is used to iterate (loop) over a sequence like:
List
Tuple
String
Dictionary
Set
Or any iterable object
'''

#✅ 1. Basic Syntax

'''for variable in iterable:
    # block of code
Example:'''

for i in [1, 2, 3]:
    print(i)

#✅ 2. Looping with range()

''''🔹 Syntax:
range(start, stop, step)
start: starting number (default is 0)
stop: number at which loop stops (excluded)
step: increment (default is 1)
Examples:'''

for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

for i in range(10, 0, -2):  # 10, 8, ..., 2
    print(i)

#✅ 3. Looping Over a String

name = "PYTHON"
for char in name:
    print(char)


#✅ 4. Looping Over a List

colors = ["red", "green", "blue"]
for color in colors:
    print(color)

#✅ 5. Looping Over a Tuple

nums = (10, 20, 30)
for n in nums:
    print(n)

#✅ 6. Looping Over a Dictionary

student = {"name": "John", "age": 20}

# Loop over keys
for key in student:
    print(key)

# Loop over keys and values
for key, value in student.items():
    print(key, ":", value)

#✅ 7. Looping Over a Set

s = {1, 2, 3}
for item in s:
    print(item)

#✅ 8. Using break in a for loop

#Stops the loop when a condition is met.


for i in range(10):
    if i == 5:
        break
    print(i)

#✅ 9. Using continue in a for loop
#Skips the current iteration and continues the loop.

for i in range(5):
    if i == 2:
        continue
    print(i)

#✅ 10. Using else with a for loop
#The else block runs only if the loop completes normally (no break).

for i in range(5):
    print(i)
else:
    print("Loop completed")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't run")

#✅ 11. Nested for Loops
#Loop inside another loop.


for i in range(1, 3):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
#✅ 12. for loop with enumerate()
#Gives index and value while iterating.


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

#✅ 13. for loop with zip()
#Used to iterate multiple lists in parallel.

names = ["Alice", "Bob"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)

#✅ 14. List Comprehension (Compact for loop)

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]

#✅ 15. Iterating with reversed()

for i in reversed(range(1, 6)):
    print(i)

#✅ 16. Iterating with sorted()

nums = [5, 2, 8, 1]
for i in sorted(nums):
    print(i)

#✅ 17. Iterating with range(len())
#Used when index is needed.


names = ["Tom", "Jerry"]

for i in range(len(names)):
    print(i, names[i])

#✅ 18. Looping Through Nested Data Structures

matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for val in row:
        print(val)

#✅ 19. Practical Examples
#🔸 Print table of 5

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#🔸 Count vowels in a string

s = "hello world"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)


'''✅ Summary Table
Concept	               Description/Use Case
Basic for	           Loop over sequences (list, str, etc.)
range()	               Loop over numbers
break, continue, else  Control flow
enumerate()	           Get index + value
zip()	               Loop over multiple sequences
nested for	           Loop inside loop
list comprehension	   Shorter way to create lists
reversed() / sorted()  Loop in reverse or sorted order
'''

#✅ 1. FizzBuzz (Amazon, Meta)
'''🧠 Problem:
Print numbers from 1 to n. For multiples of 3, print "Fizz",
for 5 print "Buzz", and for both, print "FizzBuzz".
'''

n = 15
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#✅ 2. Count Characters (Google, Amazon)
'''🧠 Problem:
Count the frequency of each character in a string.
'''

s = "google"
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)  # Output: {'g': 2, 'o': 2, 'l': 1, 'e': 1}

#✅ 3. Two Sum (Amazon, Facebook)
'''🧠 Problem:
Given a list of integers and a target, return
indices of the two numbers such that they add up to target.
'''

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])  # Output: [0, 1]
            break

#✅ 4. Reverse a String (Apple)
'''🧠 Problem:
Reverse a string using a for loop.
'''

s = "hello"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print(reversed_s)  # Output: "olleh"

#✅ 5. Move Zeroes to End (Amazon)
'''🧠 Problem:
Move all 0's to the end of the list while maintaining the order of non-zero elements.
'''

nums = [0, 1, 0, 3, 12]
res = []

for num in nums:
    if num != 0:
        res.append(num)

zero_count = len(nums) - len(res)
res += [0] * zero_count

print(res)  # Output: [1, 3, 12, 0, 0]

#✅ 6. Find Missing Number in Range 0 to n (Facebook)

nums = [3, 0, 1]
n = len(nums)
total = n * (n + 1) // 2

for num in nums:
    total -= num

print("Missing number:", total)  # Output: 2

#✅ 7. Is Anagram (Amazon, Meta)

s = "listen"
t = "silent"

if sorted(s) == sorted(t):
    print("Anagram")
else:
    print("Not Anagram")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in t:
    if char in freq:
        freq[char] -= 1
    else:
        print("Not Anagram")
        break
else:
    if all(v == 0 for v in freq.values()):
        print("Anagram")

#✅ 8. Maximum Profit in Stock Prices (Amazon, Google)

prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price

print("Max profit:", max_profit)  # Output: 5


#✅ 9. Palindrome Check (Facebook)

s = "racecar"
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break

print("Palindrome" if is_palindrome else "Not Palindrome")

#✅ 10. Find First Non-Repeating Character (Amazon)

s = "aabbccddeffg"
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in s:
    if freq[char] == 1:
        print("First non-repeating:", char)
        break


def maxProfit(prices):
    min_price = float('inf')  # Set to highest possible initially
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Example usage
prices = [7, 1, 5, 3, 6, 4]
print("Max profit:", maxProfit(prices))  # Output: 5

def firstNonRepeatingChar(s):
    freq = {}

    # First pass: count characters
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Second pass: find first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    return None


# Example usage
s = "aabbccddeffg"
print("First non-repeating character:", firstNonRepeatingChar(s))  # Output: g
