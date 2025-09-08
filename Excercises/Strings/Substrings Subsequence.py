
# 🔹 Substrings / Subsequence Problems (Q11–Q20)

# 11. Find all substrings of a string
def all_substrings_builtin(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

def all_substrings_manual(s):
    substrings = []
    n = 0
    while n < len(s):
        m = n + 1
        while m <= len(s):
            substrings.append(s[n:m])
            m += 1
        n += 1
    return substrings


# 12. Longest substring without repeating characters
def longest_unique_substring_builtin(s):
    seen, start, max_len = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

def longest_unique_substring_manual(s):
    max_len = 0
    for i in range(len(s)):
        visited = {}
        j = i
        while j < len(s) and s[j] not in visited:
            visited[s[j]] = True
            max_len = max(max_len, j - i + 1)
            j += 1
    return max_len


# 13. Longest palindromic substring
def longest_palindrome_builtin(s):
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(res):
                res = sub
    return res

def longest_palindrome_manual(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    res = ""
    for i in range(len(s)):
        p1 = expand(i, i)
        p2 = expand(i, i+1)
        res = p1 if len(p1) > len(res) else res
        res = p2 if len(p2) > len(res) else res
    return res


# 14. Longest common prefix
def longest_common_prefix_builtin(strs):
    if not strs: return ""
    prefix = min(strs)
    for s in strs:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

def longest_common_prefix_manual(strs):
    if not strs: return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        prefix = prefix[:j]
    return prefix


# 15. Longest Common Subsequence (DP)
def lcs_builtin(s1, s2):
    from functools import lru_cache
    @lru_cache(None)
    def helper(i, j):
        if i == len(s1) or j == len(s2): return 0
        if s1[i] == s2[j]:
            return 1 + helper(i+1, j+1)
        return max(helper(i+1, j), helper(i, j+1))
    return helper(0, 0)

def lcs_manual(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]


# 16. Edit Distance (Levenshtein)
def edit_distance_builtin(s1, s2):
    import Levenshtein
    return Levenshtein.distance(s1, s2)  # requires python-Levenshtein lib

def edit_distance_manual(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]


# 17. Generate all permutations
def permutations_builtin(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def permutations_manual(s):
    def backtrack(path, used, res):
        if len(path) == len(s):
            res.append("".join(path))
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                path.append(s[i])
                backtrack(path, used, res)
                path.pop()
                used[i] = False
    res = []
    backtrack([], [False]*len(s), res)
    return res


# 18. Generate all combinations
def combinations_builtin(s):
    from itertools import combinations
    res = []
    for r in range(1, len(s)+1):
        res.extend([''.join(c) for c in combinations(s, r)])
    return res

def combinations_manual(s):
    res = []
    def backtrack(start, path):
        if path:
            res.append("".join(path))
        for i in range(start, len(s)):
            path.append(s[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res


# 19. Check subsequence
def is_subsequence_builtin(s1, s2):
    it = iter(s2)
    return all(ch in it for ch in s1)

def is_subsequence_manual(s1, s2):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)


# 20. Smallest window containing all chars of another
def min_window_builtin(s, t):
    from collections import Counter
    need = Counter(t)
    have, missing, left, res = {}, len(t), 0, (0, float('inf'))
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if right-left < res[1]-res[0]:
                res = (left, right)
            need[s[left]] += 1
            missing += 1
            left += 1
    return "" if res[1] == float('inf') else s[res[0]:res[1]+1]

def min_window_manual(s, t):
    from collections import defaultdict
    need, missing = defaultdict(int), len(t)
    for ch in t: need[ch] += 1
    left, res = 0, (0, float('inf'))
    for right, ch in enumerate(s):
        if need[ch] > 0: missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right-left < res[1]-res[0]:
                res = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0: missing += 1
            left += 1
    return "" if res[1] == float('inf') else s[res[0]:res[1]+1]
