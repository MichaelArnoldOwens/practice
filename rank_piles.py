'''
❓ PROMPT
Given an array of integers representing piles of rocks (e.g., *3* means *3 rocks*), modify the input array to rank the piles from 1 to N, representing the relative sizes of each pile of rocks from smallest to largest.

That is, the pile with the lowest count of rocks should be ranked *1*, the second lowest should be *2*, and so on.

You may use built-in functions provided by your programming language.

Example(s)
Input: [3, 4, 1]
Output: [2, 3, 1]
Explanation: The last index has the smallest pile with 1 rock, so it's ranked 1st place. The first index has the 2nd smallest pile with 3 rocks, so it's ranked 2nd place. The middle index has the 3rd smallest pile with 4 rocks, so it's ranked 3rd place.

Input: [80, 27, 55, 30, 15, 90, 10]
Output: [6, 3, 5, 4, 2, 7, 1]
Explanation:
10 -> 1
15 -> 2
27 -> 3
30 -> 4
55 -> 5
80 -> 6
90 -> 7
The last index has the smallest pile with 10 rocks, so it's ranked 1st place. The 2nd smallest pile has 15 rocks, so it's ranked 2nd place. The 3rd smallest pile has 27 rocks, so it's ranked 3rd place. So on and so forth until the 7th smallest pile has 90 rocks, so it's ranked 7th place.

Input: [2, 1]
Output: [2, 1]
'''

def rank_piles(arr):
    copy_arr = arr.copy()
    copy_arr.sort()
    result = []
    sorted_dic = {}
    for i, n in enumerate(copy_arr):
        sorted_dic[n] = i + 1

    for n in arr:
        result.append(sorted_dic[n])

        
    return result


test1 = [3, 4, 1]
test2 = [80, 27, 55, 30, 15, 90, 10]
print(rank_piles(test1))
print(rank_piles(test2))
