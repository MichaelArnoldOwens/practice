'''
Formation is trying to assign a group of Fellows algorithms of varying difficulty levels. The algorithm difficulty should feel fair to all Fellows based on each Fellow's algorithmic skill level.

We are given an array of integers representing the skill level of each Fellow, and we are asked to return an array of integers representing the difficulty of an algorithm to assign each Fellow respectively.

The minimum difficulty is 1. When a Fellow has a higher skill level than an adjacent Fellow they must be given a more difficult problem than their neighbor. When a fellow has the same skill level, they must be given a problem at the same difficulty level. Return the array of difficulties representing the minimum difficulty we can give each Fellow.
 

EXAMPLE(S)
fellows = [10, 20, 60, 70, 50, 10, 20]
assignAlgorithms(fellows) -> [1,2,3,4,2,1,2]
 

FUNCTION SIGNATURE
def assignAlgorithms(fellows: list[int]) -> list[int]:

approaches / ideas
- O(n^2) find all local minima (any fellow who is less able than both neighbors), assign lowest difficuty, iterate outward in both directions
- O(2n) start with result of all 1s, work though list looking at previous, incrementing difficulty to fit rules as you go, then do the same from back to front, looking at next as you go
- O(n^2) O(n) create a hash to map skill to difficulty, then review values repeatedly to adjust to fit the constraints
- O(n^2) walk though the list, figuring out the max of how many continuous elements to the left and right it is bigger than, assign it that difficulty + 1


- O(2n) start with result of all 1s, work though list looking at previous, incrementing difficulty to fit rules as you go, then do the same from back to front, looking at next as you go



follow-up: https://leetcode.com/problems/push-dominoes/description/
'''
