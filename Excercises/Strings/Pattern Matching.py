
# 🔹 Pattern Matching (Q21–Q30)


# 21. Naive Pattern Matching
def naive_pattern_builtin(text, pattern):
    return [i for i in range(len(text)-len(pattern)+1) if text[i:i+len(pattern)] == pattern]

def naive_pattern_manual(text, pattern):
    matches = []
    for i in range(len(text)-len(pattern)+1):
        j = 0
        while j < len(pattern) and text[i+j] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i)
    return matches


# 22. KMP Algorithm
def kmp_builtin(text, pattern):
    import re
    return [m.start() for m in re.finditer(f'(?={pattern})', text)]

def kmp_manual(text, pattern):
    def build_lps(p):
        lps, j = [0]*len(p), 0
        for i in range(1, len(p)):
            while j > 0 and p[i] != p[j]:
                j = lps[j-1]
            if p[i] == p[j]:
                j += 1; lps[i] = j
        return lps
    lps, res, j = build_lps(pattern), [], 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                res.append(i-j+1)
                j = lps[j-1]
    return res


# 23. Rabin-Karp Algorithm
def rabin_karp_builtin(text, pattern):
    return naive_pattern_builtin(text, pattern)  # built-in fallback

def rabin_karp_manual(text, pattern, d=256, q=101):  # q = prime
    n, m = len(text), len(pattern)
    h, p, t, res = pow(d, m-1) % q, 0, 0, []
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    for i in range(n-m+1):
        if p == t and text[i:i+m] == pattern:
            res.append(i)
        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0: t += q
    return res


# 24. Z Algorithm
def z_algorithm_builtin(text, pattern):
    return naive_pattern_builtin(text, pattern)

def z_algorithm_manual(text, pattern):
    concat = pattern + "$" + text
    n, Z = len(concat), [0]*len(concat)
    l = r = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r-i+1, Z[i-l])
        while i+Z[i] < n and concat[Z[i]] == concat[i+Z[i]]:
            Z[i] += 1
        if i+Z[i]-1 > r:
            l, r = i, i+Z[i]-1
    res = []
    for i in range(len(pattern)+1, n):
        if Z[i] == len(pattern):
            res.append(i-len(pattern)-1)
    return res


# 25. Find all occurrences of substring
def find_occurrences_builtin(text, pattern):
    import re
    return [m.start() for m in re.finditer(f'(?={pattern})', text)]

def find_occurrences_manual(text, pattern):
    return naive_pattern_manual(text, pattern)


# 26. Check if a string is rotation of another
def is_rotation_builtin(s1, s2):
    return len(s1) == len(s2) and s2 in (s1+s1)

def is_rotation_manual(s1, s2):
    if len(s1) != len(s2): return False
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    return False


# 27. Check if two strings are anagrams
def is_anagram_builtin(s1, s2):
    return sorted(s1) == sorted(s2)

def is_anagram_manual(s1, s2):
    if len(s1) != len(s2): return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count: return False
        count[ch] -= 1
        if count[ch] < 0: return False
    return True


# 28. Group anagrams
def group_anagrams_builtin(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)
    return list(groups.values())

def group_anagrams_manual(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(list(s)))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


# 29. Check if two strings are isomorphic
def is_isomorphic_builtin(s, t):
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))

def is_isomorphic_manual(s, t):
    if len(s) != len(t): return False
    map_s, map_t = {}, {}
    for i in range(len(s)):
        if (s[i] in map_s and map_s[s[i]] != t[i]) or \
           (t[i] in map_t and map_t[t[i]] != s[i]):
            return False
        map_s[s[i]] = t[i]
        map_t[t[i]] = s[i]
    return True


# 30. Check if scrambled version
def is_scramble_builtin(s1, s2):
    from functools import lru_cache
    @lru_cache(None)
    def helper(a, b):
        if a == b: return True
        if sorted(a) != sorted(b): return False
        for i in range(1, len(a)):
            if (helper(a[:i], b[:i]) and helper(a[i:], b[i:])) or \
               (helper(a[:i], b[-i:]) and helper(a[i:], b[:-i])):
                return True
        return False
    return helper(s1, s2)

def is_scramble_manual(s1, s2):
    return is_scramble_builtin(s1, s2)  # recursion is manual logic itself
