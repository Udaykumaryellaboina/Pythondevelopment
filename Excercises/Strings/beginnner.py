

# 🔹 Beginner Level (Basics) — Q1 to Q10

#(Python with **built-in** + **manual**)

# 1. Reverse a string
def reverse_string_builtin(s):
    return s[::-1]

def reverse_string_manual(s):
    rev = ""                                                                          
    for ch in s:
        rev = ch + rev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    return rev


# 2. Check if a string is palindrome
def is_palindrome_builtin(s):
    return s == s[::-1]

def is_palindrome_manual(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

# 3. Find length of a string
def string_length_builtin(s):
    return len(s)

def string_length_manual(s):
    count = 0
    for _ in s:
        count += 1
    return count


# 4. Count vowels and consonants
def count_vc_builtin(s):
    vowels = set("aeiouAEIOU")
    v = sum(1 for ch in s if ch in vowels)
    c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v, c

def count_vc_manual(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c


# 5. Convert to uppercase/lowercase
def to_upper_builtin(s):
    return s.upper()

def to_lower_builtin(s):
    return s.lower()

def to_upper_manual(s):
    result = ""
    for ch in s:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

def to_lower_manual(s):
    result = ""
    for ch in s:
        if "A" <= ch <= "Z":
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result


# 6. Remove whitespaces
def remove_spaces_builtin(s):
    return s.replace(" ", "")

def remove_spaces_manual(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result


# 7. Count frequency of each character
def char_freq_builtin(s):
    from collections import Counter
    return dict(Counter(s))

def char_freq_manual(s):
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq


# 8. First non-repeating character
def first_non_repeat_builtin(s):
    from collections import Counter
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

def first_non_repeat_manual(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


# 9. Replace spaces with %20 (URLify)
def urlify_builtin(s):
    return s.replace(" ", "%20")

def urlify_manual(s):
    result = ""
    for ch in s:
        if ch == " ":
            result += "%20"
        else:
            result += ch
    return result


# 10. Compare two strings
def compare_builtin(s1, s2):
    return s1 == s2

def compare_manual(s1, s2):
    if string_length_manual(s1) != string_length_manual(s2):
        return False
    for i in range(string_length_manual(s1)):
        if s1[i] != s2[i]:
            return False
    return True
