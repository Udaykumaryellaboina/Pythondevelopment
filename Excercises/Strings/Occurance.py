''' Find all occurrences of a substring in a given string by ignoring the case
 Write a program to find all occurrences of “USA” in a given string ignoring the case.
 str1 = "Welcome to USA. usa awesome, isn't it?"
 expected ans --> USA:-->2'''

str1 = "Welcome to USA. usa awesome, isn't it?"
str2=str1.upper()
print(str2)
str2.count("USA")


#🔢 1. Using count() – Count Occurrence
"Counts non-overlapping occurrences of a substring."

s = "banana"
print(s.count('a'))        # Output: 3
print(s.count('an'))       # Output: 2

#🔍 2. Using find() – First Occurrence
"Returns the first index of the substring or -1 if not found."

s = "banana"
print(s.find('a'))         # Output: 1
print(s.find('z'))         # Output: -1

#🔍 3. Using rfind() – Last Occurrence
"Returns the last index of the substring or -1 if not found."

s = "banana"
print(s.rfind('a'))        # Output: 5

#🔍 4. Using index() – First Occurrence (Throws Error if Not Found)

s = "banana"
print(s.index('n'))        # Output: 2
# print(s.index('z'))      # ValueError

#🔍 5. Using rindex() – Last Occurrence (Throws Error if Not Found)
s = "banana"
print(s.rindex('n'))       # Output: 4

#🔁 6. Using Loop with if – Count Character/Substring

s = "banana"
target = 'a'
count = 0
for ch in s:
    if ch == target:
        count += 1
print(count)               # Output: 3

#🔁 7. Using for Loop with Substring Match

s = "banana"
target = "an"
count = 0
for i in range(len(s) - len(target) + 1):
    if s[i:i+len(target)] == target:
        count += 1
print(count)               # Output: 2

#🎯 8. Find All Indexes of a Character

s = "banana"
target = 'a'
indexes = [i for i, ch in enumerate(s) if ch == target]
print(indexes)             # Output: [1, 3, 5]

#🎯 9. Find All Indexes of a Substring
s = "banana"
target = "an"
indexes = []
for i in range(len(s) - len(target) + 1):
    if s[i:i+len(target)] == target:
        indexes.append(i)
print(indexes)             # Output: [1, 3]

#✅ 10. Using re.findall() – Regex for Substring Occurrence

import re
s = "banana"
print(len(re.findall('an', s)))  # Output: 2

#✅ 11. Using re.finditer() – All Match Positions
import re
s = "banana"
for match in re.finditer("an", s):
    print(match.start())         # Output: 1, 3

#⚠️ 12. Count Overlapping Substrings
"Python’s count() doesn’t handle overlapping substrings. Use a loop instead:"

s = "aaaa"
target = "aa"
count = 0
for i in range(len(s)):
    if s[i:i+len(target)] == target:
        count += 1
print(count)   # Output: 3 (overlapping: aa, aa, aa)