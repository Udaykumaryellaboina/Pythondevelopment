'''Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


'''219. Contains Duplicate II

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Constraints:
1 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9
0 <= k <= 105'''

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Stores the last seen index of each number

        for i, num in enumerate(nums):
            if num in index_map:
                if i - index_map[num] <= k:
                    return True  # Duplicate found within distance k
            index_map[num] = i  # Update the last seen index
        return False  # No such duplicate found

"""🔍 How it Works:
We use a dictionary index_map to store the last index where each number appeared.

For each number, we check:

Has it appeared before?

If yes, is the distance between current index and last index ≤ k?

If yes → return True

If not → update the index in index_map

If we go through the entire list and never find such a pair, return False.

📘 Example 1:
Input: nums = [1, 2, 3, 1], k = 3
Steps:
Index i	Value num	Seen Before?	Last Index	Distance	Action
0	1	❌ No	-	-	Save 1 → index_map[1] = 0
1	2	❌ No	-	-	Save 2 → index_map[2] = 1
2	3	❌ No	-	-	Save 3 → index_map[3] = 2
3	1	✅ Yes	0	3	3 ≤ 3 → ✅ return True

✅ Output: True

📘 Example 2:
Input: nums = [1, 0, 1, 1], k = 1
Steps:
Index i	Value num	Seen Before?	Last Index	Distance	Action
0	1	❌ No	-	-	Save 1 → index_map[1] = 0
1	0	❌ No	-	-	Save 0 → index_map[0] = 1
2	1	✅ Yes	0	2	2 > 1 → Update index_map[1] = 2
3	1	✅ Yes	2	1	1 ≤ 1 → ✅ return True

✅ Output: True

📘 Example 3:
Input: nums = [1, 2, 3, 1, 2, 3], k = 2
Steps:
Index i	Value num	Seen Before?	Last Index	Distance	Action
0	1	❌ No	-	-	Save 1 → index_map[1] = 0
1	2	❌ No	-	-	Save 2 → index_map[2] = 1
2	3	❌ No	-	-	Save 3 → index_map[3] = 2
3	1	✅ Yes	0	3	3 > 2 → Update index_map[1] = 3
4	2	✅ Yes	1	3	3 > 2 → Update index_map[2] = 4
5	3	✅ Yes	2	3	3 > 2 → Update index_map[3] = 5

❌ No duplicates found within distance ≤ k → Return False"""