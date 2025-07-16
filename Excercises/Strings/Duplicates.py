#✅ 1. Finding Duplicate Characters in a String
#🔹 Using a Dictionary:

def find_duplicate_characters(s):
    s = s.replace(" ", "")  # Optional: remove spaces
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    duplicates = {k: v for k, v in freq.items() if v > 1}
    return duplicates

s = "programming"
print(find_duplicate_characters(s))
# Output: {'r': 2, 'g': 2, 'm': 2}

#🔹 Using collections.Counter:

from collections import Counter

s = "mississippi"
counter = Counter(s)
duplicates = {k: v for k, v in counter.items() if v > 1}
print(duplicates)
# Output: {'i': 4, 's': 4, 'p': 2}

#✅ 2. Finding Duplicate Words in a Sentence
#🔹 Using Dictionary

def find_duplicate_words(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    duplicates = {k: v for k, v in freq.items() if v > 1}
    return duplicates

sentence = "This is a test this is only a test"
print(find_duplicate_words(sentence))
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2}

#🔹 Using collections.Counter:

from collections import Counter

sentence = "Python is great and Python is easy"
words = sentence.lower().split()
counter = Counter(words)
duplicates = {k: v for k, v in counter.items() if v > 1}
print(duplicates)
# Output: {'python': 2, 'is': 2}
#✅ 3. Bonus: Print Only Duplicate Elements (No Count)
#🔹 For Characters:

s = "success"
duplicates = set([ch for ch in s if s.count(ch) > 1])
print(duplicates)  # Output: {'s', 'c'}

#🔹 For Words:

sentence = "hello world hello python world"
words = sentence.lower().split()
duplicates = set([word for word in words if words.count(word) > 1])
print(duplicates)  # Output: {'hello', 'world'}