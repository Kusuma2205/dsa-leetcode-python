"""
Day 1 - DSA Journey (LeetCode)

Problem: Two Sum
LeetCode No: 1
Link: https://leetcode.com/problems/two-sum/
Date: 19-02-2026
Language: Python

----------------------------------------
Problem Faced During Practice:
----------------------------------------
While solving the problem, I initially wrote a brute force approach
using two loops but made an index mistake by starting the inner loop
from 1 instead of i+1.

This caused the same element to be used twice in some test cases.

Example:
nums = [2,5,5,11]
target = 10

My Wrong Output:
[1,1]

Expected Output:
[1,2]

Reason:
The loop was checking nums[1] + nums[1] = 5 + 5,
which means I was using the same index twice,
which is not allowed in the problem.

----------------------------------------
Initial Approach (Brute Force - Wrong Logic)
----------------------------------------

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

----------------------------------------
Corrected Brute Force Approach
----------------------------------------
Start the inner loop from i+1 to avoid using
the same element twice.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


