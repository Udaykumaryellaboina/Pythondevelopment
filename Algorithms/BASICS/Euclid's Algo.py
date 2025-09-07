"""Great 👍
Let’s go step by step into **Euclid’s Algorithm** — one of the oldest (over 2000 years old!) and most elegant algorithms. I’ll explain it in **layman’s terms**, with **examples + Python code**.

---

# 🔹 Problem Statement

We want to find the **GCD (Greatest Common Divisor)** of two numbers.

👉 Example:

```
GCD(48, 18) = 6
```

Because 6 is the largest number that divides both 48 and 18.

---

# 🔹 Naive Way

* List all divisors of both numbers.
* Pick the largest common divisor.

This is slow for large numbers.

---

# 🔹 Euclid’s Algorithm (Basic Idea)

👉 The GCD of two numbers doesn’t change if you replace the **larger number** with its **remainder** when divided by the smaller number.

Formally:

```
GCD(a, b) = GCD(b, a % b)
```

Keep doing this until one number becomes `0`. The other number is the GCD.

---

# 🔹 Layman’s Terms Explanation

Imagine you have **48 chocolates** and your friend has **18 chocolates**. You want to divide them into **equal groups with no chocolates left over**.

* Try to make groups of size 18:

  * 48 ÷ 18 = 2 groups (remainder 12).
  * So, problem reduces to GCD(18, 12).

* Now, 18 ÷ 12 = 1 group (remainder 6).

  * Problem reduces to GCD(12, 6).

* Now, 12 ÷ 6 = 2 groups (remainder 0).

  * Problem reduces to GCD(6, 0).

✅ Answer = 6.

---

# 🔹 Step by Step Example

Find `GCD(48, 18)`

1. `48 % 18 = 12` → GCD(48,18) = GCD(18,12)
2. `18 % 12 = 6`  → GCD(18,12) = GCD(12,6)
3. `12 % 6 = 0`   → GCD(12,6) = GCD(6,0)
4. ✅ GCD = 6

---

# 🔹 Python Code with Explanation

```python"""
def gcd(a, b):
    while b != 0:        # keep looping until remainder is 0
        a, b = b, a % b  # update (a, b)
    return a

# Example usage
print("GCD of 48 and 18 is:", gcd(48, 18))
"""```

---

# 🔹 Output

```
GCD of 48 and 18 is: 6
```

---

# 🔹 Time & Space Complexity

* **Time:** `O(log(min(a, b)))` → very fast, even for huge numbers.
* **Space:** `O(1)` (just two variables).

---

# 🔹 Variants

1. **Recursive version**:

```python
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
```

2. **Extended Euclidean Algorithm**:

   * Not only finds GCD, but also integers `x` and `y` such that:

     ```
     ax + by = gcd(a, b)
     ```
   * Useful in cryptography (RSA, modular inverse).

---

# 🔹 Real-Life Analogy

Think of splitting candies into groups:

* If you can’t make equal groups, you pass the leftover to your friend.
* Keep repeating until leftovers = 0.
* The group size that worked last is the **GCD**.

---

👉 Do you want me to also explain the **Extended Euclid’s Algorithm** (with the coefficients `x` and `y`), since it’s heavily used in modular arithmetic and cryptography?
"""