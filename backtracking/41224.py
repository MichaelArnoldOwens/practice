'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


'''
from typing import List


def permute(nums):
    result = []

    def helper(soFar: List[int], remaining: List[int]):
        nonlocal result
        if len(remaining) == 0:
            result.append(soFar.copy())
        for i in remaining:
            soFar = soFar.copy()
            soFar.append(i)
            newRemaining = remaining.copy()
            newRemaining.remove(i)
            helper(soFar, newRemaining)
            soFar.pop()

    if nums:
        helper([], nums)
    return result


print(permute([1, 2, 3]))