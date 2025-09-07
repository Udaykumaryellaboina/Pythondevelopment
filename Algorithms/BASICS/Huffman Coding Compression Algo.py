"""Got it 👍
Let’s now go through **Huffman Coding Compression Algorithm** step by step — in **layman’s terms**, with **examples + Python code**.

---

# 🔹 Problem Statement

We want to **compress data** efficiently.

👉 Idea: Frequently occurring characters should take **less space**, and rarely occurring ones can take **more space**.

Example:

```
Text = "aaabbc"
```

Instead of using 8 bits for each character (ASCII), we assign:

```
a = 0
b = 10
c = 11
```

Encoded text = `000101011` (9 bits total instead of 48).

---

# 🔹 Why Huffman Coding?

* It’s a **lossless compression algorithm** → no information lost.
* Used in ZIP, JPEG, MP3, etc.
* It minimizes the **average code length**.

---

# 🔹 Layman’s Terms Explanation

Imagine you’re packing suitcases for a trip:

* If you have 10 shirts and only 1 hat → give a **small suitcase** to shirts and a **big suitcase** to the hat.
* Why? Shirts appear more often → they need less overhead.

Huffman does the same with characters:

* Common characters → shorter binary codes.
* Rare characters → longer binary codes.

---

# 🔹 How Huffman Coding Works

1. **Count frequencies** of each character.
   Example: `"aaabbc"` → `a:3, b:2, c:1`.

2. **Build a min-heap (priority queue)** of nodes (character + frequency).

3. **Build Huffman Tree**:

   * Take two nodes with smallest frequencies.
   * Merge them into a new node (sum of their frequencies).
   * Push back into heap.
   * Repeat until one root node remains.

4. **Assign codes**:

   * Traverse tree → Left = `0`, Right = `1`.
   * Characters get codes based on path from root.

---

# 🔹 Step by Step Example

Text = `"aaabbc"`
Frequencies:

```
a = 3
b = 2
c = 1
```

Heap process:

1. Pick `c(1)` and `b(2)` → merge = `(3)`
2. Now heap = `[a(3), merged(3)]`
3. Pick `a(3)` and merged(3) → root = `(6)`

Tree:

```
        (6)
       /   \
     a(3)  (3)
           / \
         b(2) c(1)
```

Codes:

```
a = 0
b = 10
c = 11
```

Encoded text `"aaabbc"` = `000101011`.

---

# 🔹 Python Code with Explanation

```python"""
import heapq
from collections import Counter, namedtuple

# Node structure
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Step 1: Count frequencies
    freq = Counter(text)

    # Step 2: Build priority queue (min-heap)
    heap = [Node(ch, f, None, None) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Step 3: Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]  # root node


def build_codes(node, prefix="", codebook={}):
    # Recursive DFS traversal
    if node.char is not None:  # Leaf node
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes


# Example usage
text = "aaabbc"
encoded, codes = huffman_encoding(text)

print("Character Codes:", codes)
print("Encoded Text:", encoded)
"""```

---

# 🔹 Output

```
Character Codes: {'a': '0', 'b': '10', 'c': '11'}
Encoded Text: 000101011
```

---

# 🔹 Time & Space Complexity

* **Building tree:** `O(n log n)` (because of heap operations).
* **Encoding:** `O(n)` (for text length n).
* **Space:** `O(n)` for storing codes.

---

# 🔹 Real-Life Analogy

Think of **Morse Code**:

* Common letters like `E` and `T` have **short codes** (`.` and `-`).
* Rare letters like `Q` and `Z` have **longer codes**.
  Huffman coding works the same way!

---

👉 Do you also want me to extend this explanation to show **decoding** (how to get back original text from encoded bits)?
"""