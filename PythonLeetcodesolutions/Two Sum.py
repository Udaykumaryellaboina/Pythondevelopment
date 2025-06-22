"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
•2 <= nums.length <= 104
•-109 <= nums[i] <= 109
•-109 <= target <= 109
•Only one valid answer exists."""

#Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
#Using HashMap -->O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # To store number as key and its index as value

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

"""Step-by-Step Execution:

Initialize an empty dictionary:
num_map = {}
Start iterating over nums using enumerate:

Iteration 1:
i = 0
num = 2
complement = target - num = 9 - 2 = 7
Check: Is 7 in num_map? → ❌ No
Action: Add 2: 0 to the dictionary
num_map = {2: 0}

▶️ Iteration 2:
i = 1
num = 7
complement = 9 - 7 = 2
Check: Is 2 in num_map? → ✅ Yes, num_map[2] = 0
Action: Return [num_map[2], i] → [0, 1]

✅ Final Output:
[0, 1]
This means nums[0] + nums[1] = 2 + 7 = 9.

🔚 Execution Ends Here (early return once the pair is found)"""


"""
Way 1 --> Brute force -->O(n2)
simply check if ith element is making a pair with any of the other element on
the right side"""


class Solution1:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
✅ Way 1: Brute Force (O(n²))
For each element nums[i], check every element to its right nums[j].
If nums[i] + nums[j] == target, return [i, j].

🔁 Dry Run:
Input:
nums = [2, 7, 11, 15], target = 9
i = 0 → nums[0] = 2
→ j = 1 → nums[1] = 7
→ 2 + 7 = 9 ✅ → return [0, 1]

✅ Output:
[0, 1]
✅ Pros:
Simple and easy to understand
No extra memory used
❌ Cons:
Very slow for large input sizes (O(n²))
"""


"""Way 2-->Using Two Pointer approach-->O(n log n )
time complexity is nlogn because in this approach, the array will be first sorted and then ,
two pointer approach will be used
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()  # Sort by value

        left, right = 0, len(nums) - 1
        while left < right:
            sum_val = nums_with_index[left][0] + nums_with_index[right][0]
            if sum_val == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif sum_val < target:
                left += 1
            else:
                right -= 1


"""Way 2: Two Pointer Approach (O(n log n))
⚠️ Note:
This approach only works if you're allowed to sort the array and you want to return the values,
 not the original indices — unless you track the indices separately (we will!).

🔍 Logic:
Store each number with its index.
Sort based on values.
Use two pointers (left, right) to find two numbers whose sum equals target.
🔁 Dry Run:
Input:
nums = [2, 7, 11, 15], target = 9

Create list with indices:

[(2,0), (7,1), (11,2), (15,3)]

Already sorted
Start:
left = 0 → 2
right = 3 → 15
sum = 17 ❌ → move right to 2
left = 0, right = 2 → 2 + 11 = 13 ❌
left = 0, right = 1 → 2 + 7 = 9 ✅ → return [0, 1]

✅ Output:
[0, 1]

✅ Pros:
Faster than brute force
Useful when you're working with sorted arrays or want to find pair of values, not just indices
❌ Cons:
Extra space to store original indices
Can't use it directly on LeetCode unless you preserve indices carefully"""

"""
Approach	    Time Complexity	  Space Complexity	      Notes
Brute Force	     O(n²)	           O(1)	                    Simple but slow
Two Pointers	 O(n log n)	       O(n)	                    Requires sorting + index tracking
HashMap (Best)	 O(n)	           O(n)	                    Optimal solution
"""