
# 🧩 Leetcode 238: Product of Array Except Self
## 🔶 **Problem Statement**

'''Given an array of integers `nums`, return an array `answer` such that:
answer[i] = product of all elements in nums except nums[i]

### 🔒 Constraints:

* You **cannot use division**.
* Solution must run in **O(n)** time.
* Try to achieve **O(1) extra space** (excluding the output array).

## 🧪 Example 1:
**Input:**
nums = [1, 2, 3, 4]
**Output:**

[24, 12, 8, 6]

**Explanation:**

* answer\[0] = 2×3×4 = 24
* answer\[1] = 1×3×4 = 12
* answer\[2] = 1×2×4 = 8
* answer\[3] = 1×2×3 = 6

---

## ✅ Approach 1: Brute Force (O(n²) Time)

### 🔧 Idea:

Loop through the array for each element `i` and calculate the product of all elements **except** at `i`.

### 🧾 Code:'''

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    ans[i] *= nums[j]
        return ans
'''
### 📊 Time & Space:

* **Time:** O(n²) → inefficient for large arrays.
* **Space:** O(1) extra (excluding the output array).

### ✅ Pros:

* Easy to understand.

### ❌ Cons:

* Very slow for large inputs. Will result in **TLE** (Time Limit Exceeded) in interviews or contests.


## ✅ Approach 2: Prefix and Suffix Arrays (O(n) Time, O(n) Space)

### 🔧 Idea:

* Compute:

  * `prefix[i]` = product of all elements before index `i`
  * `suffix[i]` = product of all elements after index `i`
* Then:
  `answer[i] = prefix[i] * suffix[i]`

### 🧾 Code:'''

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


### 📊 Time & Space:
'''
* **Time:** O(n)
* **Space:** O(n) extra for `prefix` and `suffix`

### ✅ Pros:

* Fast and efficient
* Easier to debug than the constant space version

### ❌ Cons:

* Uses O(n) additional space

---

## ✅ Approach 3: Optimal - Prefix in Result + Suffix with Variable (O(n) Time, O(1) Space)

### 🔧 Idea:

* First pass:

  * Store prefix products directly in the result array.
* Second pass:

  * Traverse backward with a single `suffix` variable to update each result.

### 🧾 Code:'''

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Fill with prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


### 📊 Time & Space:
'''
* **Time:** O(n)
* **Space:** O(1) extra (output array not counted)

### ✅ Pros:

* Fastest and most space-efficient.
* Best solution for interviews and real-world use.

### ❌ Cons:

* Slightly more complex to understand at first glance.

---

## 🏁 Which One to Choose?

| Approach                    | Time   | Space  | Use In Interview? | When to Use?                           |
| --------------------------- | ------ | ------ | ----------------- | -------------------------------------- |
| 1. Brute Force              | O(n²)  | O(1)   | ❌ No              | Never (just for learning)              |
| 2. Prefix & Suffix Arrays   | O(n)   | O(n)   | ✅ Maybe           | When readability/debuggability matters |
| 3. Optimal (Constant Space) | ✅ O(n) | ✅ O(1) | ✅✅ Yes            | **Always prefer this**                 |

---

### ✅ Final Recommendation:

Use **Approach 3**: It is the **most optimal solution**,
 meeting all constraints (O(n) time, O(1) space, no division).
  It's also a common **interview-winning technique** that demonstrates strong problem-solving skills.'''


