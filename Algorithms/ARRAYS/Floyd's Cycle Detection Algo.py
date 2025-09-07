"""Perfect 👍
Let’s now break down **Floyd’s Cycle Detection Algorithm** (also called **Tortoise and Hare Algorithm**) in **layman’s terms** with **Python code + step-by-step explanation**.

---

# 🔹 Problem Statement

We want to check if a **linked list** has a **cycle (loop)**.

👉 A **cycle** means that while traversing the linked list, you keep going in circles and never reach `None`.

Example:

```
1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          ← ← ← ← ← 
```

Here, node `5` points back to node `3`, so it forms a cycle.

---

# 🔹 Why Not Just Use a Hash Set?

One way is to **keep a visited set of nodes**.
If we visit the same node again → cycle exists.

But that uses **extra space (O(n))**.
👉 Floyd’s Algorithm detects the cycle using **O(1) extra space** (only two pointers).

---

# 🔹 Layman’s Terms Explanation

Think of it as a **race track**:

1. A **slow runner (tortoise)** runs 1 step at a time.
2. A **fast runner (hare)** runs 2 steps at a time.

Now:

* If the track is straight (no cycle), the fast runner will reach the end (`None`).
* If the track is circular, eventually the fast runner will **lap** the slow runner (they will meet at some node).

---

# 🔹 Step by Step Example

Linked list:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
               ↑         ↓
               ← ← ← ← ← 
```

* Start: slow = 1, fast = 1
* Move 1: slow = 2, fast = 3
* Move 2: slow = 3, fast = 5
* Move 3: slow = 4, fast = 3 (they don’t meet yet)
* Move 4: slow = 5, fast = 5 ✅ They meet → cycle exists

---

# 🔹 Python Code with Explanation

```python"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    # Step 1: Create two pointers
    slow = head
    fast = head

    # Step 2: Move through the list
    while fast and fast.next:
        slow = slow.next           # Move slow by 1 step
        fast = fast.next.next      # Move fast by 2 steps

        # Step 3: Check if they meet
        if slow == fast:
            return True   # Cycle detected

    return False   # If fast reaches None, no cycle


# Example usage
# Creating a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> points back to 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next  # cycle at node 3

print("Cycle exists?" , has_cycle(head))  # Output: True
"""```

---

# 🔹 Output

```
Cycle exists? True
```

---

# 🔹 Time & Space Complexity

* **Time:** `O(n)` → In worst case, we may traverse all nodes before detecting a cycle.
* **Space:** `O(1)` → Only two pointers used.

---

# 🔹 Real-Life Analogy

Imagine a **circular jogging track**:

* A slow jogger (1 step) and a fast jogger (2 steps).
* If the track is **straight**, the fast jogger leaves the track.
* If it’s **circular**, the fast jogger eventually **laps** the slow jogger.

That’s exactly how this algorithm works 🚀

---
"""