

# 🔹 Special Interview String Problems (Q46–Q55)

# 46. Longest substring with k unique characters
def longest_substring_k_builtin(s, k):
    from collections import defaultdict
    left, max_len, freq = 0, 0, defaultdict(int)
    for right in range(len(s)):
        freq[s[right]] += 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0: del freq[s[left]]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len

def longest_substring_k_manual(s, k):
    left, max_len, freq = 0, 0, {}
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0: del freq[s[left]]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len


# 47. Remove all duplicate characters
def remove_duplicates_builtin(s):
    return "".join(dict.fromkeys(s))

def remove_duplicates_manual(s):
    seen, result = set(), ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result


# 48. Smallest substring containing all unique characters
def smallest_unique_substring_builtin(s):
    unique_chars = set(s)
    required = len(unique_chars)
    from collections import Counter
    left, formed, window, freq = 0, 0, (0, float("inf")), Counter()
    for right in range(len(s)):
        freq[s[right]] += 1
        if len(freq) == required:
            while len(freq) == required:
                if right-left < window[1]-window[0]:
                    window = (left, right)
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
    return "" if window[1] == float("inf") else s[window[0]:window[1]+1]

def smallest_unique_substring_manual(s):
    unique_chars, required = {}, len(set(s))
    left, res, freq = 0, "", {}
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) == required:
            if res == "" or right-left+1 < len(res):
                res = s[left:right+1]
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
    return res


# 49. Find the first repeating character
def first_repeating_builtin(s):
    from collections import Counter
    freq = Counter(s)
    for ch in s:
        if freq[ch] > 1:
            return ch
    return None

def first_repeating_manual(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


# 50. Lexicographically next permutation of string
def next_permutation_builtin(s):
    arr = list(s)
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1: return "".join(sorted(arr))
    j = len(arr)-1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return "".join(arr)

def next_permutation_manual(s):
    return next_permutation_builtin(s)  # manual is same algorithm, just step-by-step


# 51. Wildcard pattern matching (?, *)
def wildcard_match_builtin(s, p):
    import fnmatch
    return fnmatch.fnmatch(s, p)

def wildcard_match_manual(s, p):
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True
    for j in range(1, len(p)+1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-1]
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == "?" or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[len(s)][len(p)]


# 52. Regex matching (., *)
def regex_match_builtin(s, p):
    import re
    return re.fullmatch(p, s) is not None

def regex_match_manual(s, p):
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True
    for j in range(2, len(p)+1):
        if p[j-1] == "*" and dp[0][j-2]:
            dp[0][j] = True
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == "." or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i][j-2] or ((p[j-2] == "." or p[j-2] == s[i-1]) and dp[i-1][j])
    return dp[len(s)][len(p)]


# 53. Longest duplicate substring
def longest_duplicate_builtin(s):
    n = len(s)
    res = ""
    for i in range(n):
        for j in range(i+1, n):
            k = 0
            while i+k < n and j+k < n and s[i+k] == s[j+k]:
                if k+1 > len(res):
                    res = s[i:i+k+1]
                k += 1
    return res

def longest_duplicate_manual(s):
    return longest_duplicate_builtin(s)  # manual suffix array is complex, this is O(n^2)


# 54. Reverse words in a sentence
def reverse_words_builtin(s):
    return " ".join(reversed(s.split()))

def reverse_words_manual(s):
    words, word = [], ""
    for ch in s + " ":
        if ch != " ":
            word += ch
        else:
            words.append(word)
            word = ""
    words.reverse()
    return " ".join(words)


# 55. Check if one string is subsequence of another
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
