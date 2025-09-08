

# 🔹 Miscellaneous String Problems (Q56–Q60)

# 56. Check if two strings are rotations of each other
def are_rotations_builtin(s1, s2):
    return len(s1) == len(s2) and s2 in (s1+s1)

def are_rotations_manual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]
        if rotated == s2:
            return True
    return False


# 57. Check if string is numeric
def is_numeric_builtin(s):
    return s.isdigit()

def is_numeric_manual(s):
    if not s: return False
    for ch in s:
        if not ('0' <= ch <= '9'):
            return False
    return True


# 58. Shortest string containing two given strings as subsequences
def shortest_common_supersequence_builtin(s1, s2):
    from functools import lru_cache
    @lru_cache(None)
    def lcs(i, j):
        if i == len(s1) or j == len(s2):
            return ""
        if s1[i] == s2[j]:
            return s1[i] + lcs(i+1, j+1)
        left = lcs(i+1, j)
        right = lcs(i, j+1)
        return left if len(left) > len(right) else right

    lcs_str = lcs(0, 0)
    i = j = 0
    res = ""
    for c in lcs_str:
        while s1[i] != c:
            res += s1[i]; i += 1
        while s2[j] != c:
            res += s2[j]; j += 1
        res += c; i += 1; j += 1
    return res + s1[i:] + s2[j:]

def shortest_common_supersequence_manual(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[""]*(m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = s1[i] + dp[i+1][j+1]
            else:
                left, right = dp[i+1][j], dp[i][j+1]
                dp[i][j] = left if len(left) > len(right) else right
    lcs_str = dp[0][0]
    i = j = 0
    res = ""
    for c in lcs_str:
        while s1[i] != c:
            res += s1[i]; i += 1
        while s2[j] != c:
            res += s2[j]; j += 1
        res += c; i += 1; j += 1
    return res + s1[i:] + s2[j:]


# 59. Word break problem
def word_break_builtin(s, word_dict):
    from functools import lru_cache
    word_set = set(word_dict)
    @lru_cache(None)
    def dfs(start):
        if start == len(s): return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in word_set and dfs(end):
                return True
        return False
    return dfs(0)

def word_break_manual(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]


# 60. Print all valid IP addresses from string of digits
def restore_ip_addresses_builtin(s):
    res = []
    def backtrack(start, path):
        if len(path) == 4 and start == len(s):
            res.append(".".join(path))
            return
        if len(path) == 4: return
        for l in range(1, 4):
            if start+l > len(s): break
            part = s[start:start+l]
            if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start+l, path+[part])
    backtrack(0, [])
    return res

def restore_ip_addresses_manual(s):
    res = []
    n = len(s)
    for i in range(1, min(4, n-2)):
        for j in range(i+1, min(i+4, n-1)):
            for k in range(j+1, min(j+4, n)):
                a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                if all(map(valid_ip_part, [a, b, c, d])):
                    res.append(".".join([a, b, c, d]))
    return res

def valid_ip_part(part):
    if not part or (part.startswith("0") and len(part) > 1):
        return False
    if not part.isdigit() or int(part) > 255:
        return False
    return True
