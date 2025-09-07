"""Awesome 👍
Let’s now carefully explain **Boyer–Moore Majority Vote Algorithm** step by step in **layman’s terms** with **examples + Python code**, just like we did for Kadane, Floyd, KMP, and Quick Select.

---

# 🔹 Problem Statement

We want to find the **majority element** in an array.

👉 A **majority element** = an element that appears **more than n/2 times** in an array of size `n`.

Example:

```
arr = [3, 3, 4, 2, 3, 3, 5, 3]
```

Here, `3` appears 5 times out of 8 → majority element = `3`.

---

# 🔹 The Naive Way

* Count frequency of every element (using dictionary/hashmap).
* Time: `O(n)`, Space: `O(n)`.

But can we do this in **O(n) time and O(1) space**?
👉 Yes → That’s what **Boyer–Moore Algorithm** does. 🚀

---

# 🔹 Layman’s Terms Explanation

Imagine you’re voting for a class monitor:

* Every student votes.
* You’re counting votes **pairwise**:

  * If two students vote for different candidates → cancel both votes.
  * If same → keep one.

At the end:

* The candidate left (if any) is the **majority candidate**.

Why does this work?
Because the majority candidate (appearing more than n/2) can’t be completely canceled out by others.

---

# 🔹 Step by Step Example

Array: `[3, 3, 4, 2, 3, 3, 5, 3]`

1. Start: candidate = None, count = 0
2. Read `3`: count = 1, candidate = 3
3. Read `3`: count = 2
4. Read `4`: count = 1
5. Read `2`: count = 0 (canceled)
6. Read `3`: count = 1, candidate = 3
7. Read `3`: count = 2
8. Read `5`: count = 1
9. Read `3`: count = 2

End → candidate = 3 ✅

(Then verify if it actually appears > n/2 times).

---

# 🔹 Python Code with Explanation

```python"""
def majority_element(nums):
    # Step 1: Find candidate using Boyer-Moore
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Step 2: Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None


# Example usage
arr = [3, 3, 4, 2, 3, 3, 5, 3]
print("Majority element is:", majority_element(arr))
"""```

---

# 🔹 Output

```
Majority element is: 3
```

---

# 🔹 Time & Space Complexity

* **Time:** `O(n)`
* **Space:** `O(1)` (constant space, just two variables).

---

# 🔹 Real-Life Analogy

Think of a **debate hall**:

* Every time two people with opposite views meet → they cancel each other out.
* Only the side with the majority (more than half) will remain till the end.

That’s the Boyer–Moore algorithm.

---

👉 Do you also want me to extend this and show how it can be modified to find elements that appear **more than n/3 times** (the generalization of Boyer–Moore)?
"""