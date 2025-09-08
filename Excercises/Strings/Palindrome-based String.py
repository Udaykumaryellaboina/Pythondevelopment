
# 🔹 Palindrome-based String Problems (Q41–Q45)

# 41. Find all palindromic substrings
def all_palindromes_builtin(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i:j] == s[i:j][::-1]]

def all_palindromes_manual(s):
    res = []
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res.append(s[l:r+1])
            l -= 1; r += 1
    for i in range(len(s)):
        expand(i, i)      # odd length
        expand(i, i+1)    # even length
    return res


# 42. Count number of palindromic substrings
def count_palindromes_builtin(s):
    return len(all_palindromes_builtin(s))

def count_palindromes_manual(s):
    count = 0
    def expand(l, r):
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1; r += 1
    for i in range(len(s)):
        expand(i, i)
        expand(i, i+1)
    return count


# 43. Check if a string can be rearranged into a palindrome
def can_form_palindrome_builtin(s):
    from collections import Counter
    freq = Counter(s)
    odd = sum(1 for v in freq.values() if v % 2)
    return odd <= 1

def can_form_palindrome_manual(s):
    freq, odd_count = {}, 0
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for val in freq.values():
        if val % 2: odd_count += 1
    return odd_count <= 1


# 44. Minimum insertions to make a string palindrome
def min_insertions_builtin(s):
    return len(s) - lps_length_builtin(s)

def lps_length_builtin(s):
    rev = s[::-1]
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[i] == rev[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

def min_insertions_manual(s):
    n = len(s)
    rev = s[::-1]
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[i] == rev[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    lps = dp[0][0]
    return n - lps


# 45. Palindrome Partitioning (minimum cuts)
def min_cut_partition_builtin(s):
    n = len(s)
    dp = [0]*n
    pal = [[False]*n for _ in range(n)]
    for i in range(n):
        min_cut = i
        for j in range(i+1):
            if s[j] == s[i] and (i-j < 2 or pal[j+1][i-1]):
                pal[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, dp[j-1]+1)
        dp[i] = min_cut
    return dp[-1]

def min_cut_partition_manual(s):
    n = len(s)
    is_pal = [[False]*n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if length == 2 or is_pal[i+1][j-1]:
                    is_pal[i][j] = True
    dp = [0]*n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = min(dp[j]+1 for j in range(i) if is_pal[j+1][i])
    return dp[-1]
