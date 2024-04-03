'''
❓ PROMPT
Given an array and a number *X*, return an array containing every *X*th number in the input array.

Example(s)
everyXth([1,2,3,4,5,6], 2) == [2,4,6]
everyXth([1,2,3,4,5,6], 3) == [3,6]
 

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
function everyXth(arr, x) {
def everyXth(arr: list[int], x: int) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def everyXth(arr, n):
    result = []
    idx = 0
    
    while idx < len(arr):
        if idx > 0 and (idx + 1) % n == 0:
            result.append(arr[idx])
        idx += 1
    return result
print(everyXth([1,2,3,4,5,6], 2) == [2,4,6])
print(everyXth([1,2,3,4,5,6], 3) == [3,6])

