"""Great choice 👍
Let’s now break down **KMP Algorithm (Knuth–Morris–Pratt)** from scratch in **layman’s terms** with **step-by-step explanation + Python code**.

---

# 🔹 Problem Statement

We want to solve the **string pattern matching problem**:

👉 Given a **text** and a **pattern**, check if the pattern exists inside the text (and where).

Example:

```
Text    = "abxabcabcaby"
Pattern = "abcaby"
```

Answer → Pattern starts at index `6`.

---

# 🔹 The Naive Way

Normally, we compare the pattern with the text character by character:

* If mismatch → shift the pattern by **1 position** and try again.
* Worst case (like `"aaaaa....aaab"` vs `"aaab"`) → **O(n × m)** time (n = text length, m = pattern length).

---

# 🔹 Why KMP?

KMP is smarter:

* It **doesn’t re-check characters** that we already know will match.
* It uses some **preprocessing** of the pattern → builds an array called **LPS** (Longest Prefix Suffix).

---

# 🔹 Layman’s Terms Explanation

Think of it like searching for a **word in a book**:

* Instead of starting over every time you get stuck, you use a **bookmark** to remember where the next possible match can start.

That "bookmark info" is stored in the **LPS array**.

---

# 🔹 LPS (Longest Prefix Suffix) Array

For a pattern, `lps[i]` = length of the **longest prefix** of the pattern that is also a **suffix** of the substring `pattern[0..i]`.

Example:
Pattern = `"abcaby"`

* `"a"` → no proper prefix = suffix → lps = 0
* `"ab"` → no match → lps = 0
* `"abc"` → no match → lps = 0
* `"abca"` → `"a"` matches → lps = 1
* `"abcab"` → `"ab"` matches → lps = 2
* `"abcaby"` → no match → lps = 0

So, LPS = `[0, 0, 0, 1, 2, 0]`

---

# 🔹 How KMP Works

1. Build the **LPS array** for the pattern.
2. Start matching the pattern with the text:

   * If characters match → move forward.
   * If mismatch: instead of going back to start, **use LPS array to skip ahead**.

---

# 🔹 Step by Step Example

Text = `"abxabcabcaby"`
Pattern = `"abcaby"`
LPS = `[0, 0, 0, 1, 2, 0]`

* Start matching at index 0
* `abx` vs `abc` → mismatch at `x`
* Instead of restarting, LPS tells us → start from index 0 of pattern
* Continue matching… eventually match found at **index 6**

---

# 🔹 Python Code with Explanation

```python"""
def compute_lps(pattern):
    """Compute the Longest Prefix Suffix (LPS) array."""
    lps = [0] * len(pattern)
    length = 0  # length of previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # fall back
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """KMP search algorithm."""
    lps = compute_lps(pattern)
    i = j = 0  # i = text index, j = pattern index

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j  # match found at index (i - j)
        else:
            if j != 0:
                j = lps[j - 1]  # use LPS to skip
            else:
                i += 1

    return -1  # not found


# Example usage
text = "abxabcabcaby"
pattern = "abcaby"
print("Pattern found at index:", kmp_search(text, pattern))
"""```

---

# 🔹 Output

```
Pattern found at index: 6
```

---

# 🔹 Time & Space Complexity

* **Preprocessing (LPS building):** `O(m)`
* **Pattern Search:** `O(n)`
* **Total:** `O(n + m)`
* **Space:** `O(m)` for LPS array

---

# 🔹 Real-Life Analogy

Imagine you’re typing a password `"abcabc"`, and at `"abcabx"` it fails.
Instead of starting over, you realize `"ab"` is already typed correctly at the end → you don’t type it again.

That’s exactly what **KMP does** → it saves time by remembering partial matches.

---

👉 Do you want me to also extend this explanation to show how **KMP finds *all* occurrences of the pattern** in the text (not just the first one)?
"""