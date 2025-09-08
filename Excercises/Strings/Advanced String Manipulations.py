

# 🔹 Advanced String Manipulations (Q31–Q40)


# 31. Longest Repeating Substring
def longest_repeating_builtin(s):
    n = len(s)
    subs = set()
    longest = ""
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub in subs and len(sub) > len(longest):
                longest = sub
            subs.add(sub)
    return longest

def longest_repeating_manual(s):
    n, longest = len(s), ""
    for i in range(n):
        for j in range(i+1, n):
            k = 0
            while i+k < n and j+k < n and s[i+k] == s[j+k]:
                if k+1 > len(longest):
                    longest = s[i:i+k+1]
                k += 1
    return longest


# 32. Lexicographically smallest & largest substring of length k
def lex_substring_builtin(s, k):
    subs = [s[i:i+k] for i in range(len(s)-k+1)]
    return min(subs), max(subs)

def lex_substring_manual(s, k):
    smallest = largest = s[0:k]
    for i in range(1, len(s)-k+1):
        sub = s[i:i+k]
        if sub < smallest:
            smallest = sub
        if sub > largest:
            largest = sub
    return smallest, largest


# 33. Minimum bracket reversals to balance
def min_reversals_builtin(expr):
    if len(expr) % 2: return -1
    stack = []
    for ch in expr:
        if ch == '{':
            stack.append(ch)
        elif stack and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(ch)
    m = stack.count('{')
    n = len(stack) - m
    return (m+1)//2 + (n+1)//2

def min_reversals_manual(expr):
    if len(expr) % 2: return -1
    open_count = close_count = 0
    for ch in expr:
        if ch == '{':
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1
    return (open_count+1)//2 + (close_count+1)//2


# 34. Validate balanced parentheses/brackets
def is_balanced_builtin(s):
    stack, mapping = [], {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack

def is_balanced_manual(s):
    stack, opening, closing = [], "([{", ")]}"
    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if not stack: return False
            match = opening[closing.index(ch)]
            if stack[-1] != match: return False
            stack.pop()
    return not stack


# 35. Remove adjacent duplicates
def remove_adj_duplicates_builtin(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

def remove_adj_duplicates_manual(s):
    res = ""
    for ch in s:
        if res and res[-1] == ch:
            res = res[:-1]
        else:
            res += ch
    return res


# 36. Run Length Encoding (Encode/Decode)
def rle_encode_builtin(s):
    from itertools import groupby
    return "".join(ch+str(len(list(g))) for ch, g in groupby(s))

def rle_encode_manual(s):
    encoded, count = "", 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            encoded += s[i-1] + str(count)
            count = 1
    return encoded

def rle_decode(s):
    decoded, i = "", 0
    while i < len(s):
        ch, j = s[i], i+1
        num = ""
        while j < len(s) and s[j].isdigit():
            num += s[j]
            j += 1
        decoded += ch * int(num)
        i = j
    return decoded


# 37. Implement atoi() (string to integer)
def atoi_builtin(s):
    try:
        return int(s)
    except:
        return None

def atoi_manual(s):
    s = s.strip()
    if not s: return 0
    sign, i, num = 1, 0, 0
    if s[0] in "+-":
        if s[0] == '-': sign = -1
        i += 1
    while i < len(s) and '0' <= s[i] <= '9':
        num = num*10 + (ord(s[i]) - ord('0'))
        i += 1
    return sign*num


# 38. Implement strstr() (find substring)
def strstr_builtin(haystack, needle):
    return haystack.find(needle)

def strstr_manual(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


# 39. Convert integer to string (itoa)
def itoa_builtin(num):
    return str(num)

def itoa_manual(num):
    if num == 0: return "0"
    sign, res = "", ""
    if num < 0:
        sign, num = "-", -num
    while num > 0:
        res = chr(ord('0') + num % 10) + res
        num //= 10
    return sign + res


# 40. Longest word in a sentence
def longest_word_builtin(sentence):
    words = sentence.split()
    return max(words, key=len)

def longest_word_manual(sentence):
    max_word, max_len, word = "", 0, ""
    for ch in sentence + " ":
        if ch != " ":
            word += ch
        else:
            if len(word) > max_len:
                max_len, max_word = len(word), word
            word = ""
    return max_word
