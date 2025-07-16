#✅ 1. Using String Slicing (Most Pythonic Way)

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: "olleh"

#✅ 2. Using reversed() and join()
s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: "olleh"

#✅ 3. Using a Loop (Manual Reversal)
s = "hello"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)  # Output: "olleh"

#✅ 4. Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

s = "hello"
print(reverse_string(s))  # Output: "olleh"

#✅ 5. Using Stack (List as Stack)
s = "hello"
stack = list(s)
reversed_s = ""
while stack:
    reversed_s += stack.pop()
print(reversed_s)  # Output: "olleh"
#✅ 6. Using List Comprehension
s = "hello"
reversed_s = ''.join([s[i] for i in range(len(s)-1, -1, -1)])
print(reversed_s)  # Output: "olleh"
#✅ 7. Using while Loop and Index
s = "hello"
reversed_s = ""
i = len(s) - 1
while i >= 0:
    reversed_s += s[i]
    i -= 1
print(reversed_s)  # Output: "olleh"

#✅ 8. Using reduce() from functools
from functools import reduce

s = "hello"
reversed_s = reduce(lambda x, y: y + x, s)
print(reversed_s)  # Output: "olleh"

#✅ 9. Using map() with reversed() (Unusual but works)
s = "hello"
reversed_s = ''.join(map(str, reversed(s)))
print(reversed_s)  # Output: "olleh"

#✅ 10. Using a Lambda Function

reverse = lambda s: s[::-1]
print(reverse("hello"))  # Output: "olleh"


#✅ Example:
#Input: "Hello World from Python"
#Output: "olleH dlroW morf nohtyP"

#✅ 1. Using List Comprehension

sentence = "Hello World from Python"
reversed_words = ' '.join([word[::-1] for word in sentence.split()])
print(reversed_words)
# Output: "olleH dlroW morf nohtyP"


#✅ 2. Using Loop

sentence = "Hello World from Python"
words = sentence.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
result = ' '.join(reversed_words)
print(result)
# Output: "olleH dlroW morf nohtyP"


#✅ 3. Using map() Function=
sentence = "Hello World from Python"
reversed_words = ' '.join(map(lambda w: w[::-1], sentence.split()))
print(reversed_words)
# Output: "olleH dlroW morf nohtyP"

#✅ 4. With Punctuation Handling (Optional Enhancement)
"If your sentence includes punctuation, use regex to preserve it properly:"

import re

sentence = "Hello, world! Let's code."
words = re.findall(r'\b\w+\b|\W+', sentence)
reversed_sentence = ''.join([w[::-1] if w.isalnum() else w for w in words])
print(reversed_sentence)
# Output: "olleH, dlrow! s'teL edoc."