'''
❓ PROMPT
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example(s)
sumDigits(12) == 3
sumDigits(49) == 13
sumDigits(126) == 9
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function sumDigits(n) {
def sumDigits(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def helper(num):
    if num == 0:
        return 0
    return num % 10 + helper(num // 10)
def sumDigits(num):
    return helper(num)
print(sumDigits(12) == 3)
print(sumDigits(49) == 13)
print(sumDigits(126) == 9)
 
