'''
❓ PROMPT
Given an array of floats that represents the movement in the share price of a company over time, design an algorithm that determines the maximum profit that could have been made by buying and then selling a single share over the time period. The buy must occur before the sell.

Example(s)
Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
*Note: buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.*

Input: prices = [7,6,4,3,1]
Output: 0

Explanation: In this case, no transactions are done, and the max profit = 0.
'''

def maxProfitPotential(prices: list[float]) -> float:
    if len(prices) < 2:
        return 0
    low = prices[0]
    result = 0
    for i in range(1, len(prices)):
        curr = prices[i]
        if low > curr:
            low = curr
        else:
            result = max(result, curr - low)
    return result


print(maxProfitPotential([7,6,4,3,1]))
print(maxProfitPotential([7,1,5,3,6,4]))
print(maxProfitPotential([7,1,5,3,6,4, 10]))
print(maxProfitPotential([1,5,3,20, 6,4, 10]))


print(maxProfitPotential([7,1,5,3,6,4]) == 5)
print(maxProfitPotential([7,6,4,3,1]) == 0)
print(maxProfitPotential([3,1,5]) == 4)
print(maxProfitPotential([1,2,3,5,6,7]) == 6)
print(maxProfitPotential([3,3,3,3,3,3]) == 0)
print(maxProfitPotential([0.55,1.23,3.53,1.75,5.16]) == 4.61)
print(maxProfitPotential([1,9]) == 8)
print(maxProfitPotential([8,2]) == 0)
print(maxProfitPotential([1]) == 0)
print(maxProfitPotential([]) == 0)
print(maxProfitPotential([2, 5, 7, 1, 3, 4, 5]) == 5)

