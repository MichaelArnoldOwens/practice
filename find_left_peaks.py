'''
❓ PROMPT
Given an array of integers, return a sub-array of 'Left Peaks'. A Left Peak is defined as an element that is greater or equal in value to all elements to its right.

Example(s)
find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]
find_left_peaks([3, 2, 1]) => [3, 2, 1]
 

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
function find_left_peaks(arr) {
def find_left_peaks(arr: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def find_left_peaks(arr):
    idx = len(arr) - 1
    result = []
    greatest = float('-inf')
    while idx >= 0:
        curr_val = arr[idx]
        if curr_val > greatest:
            result.insert(0, curr_val)
            greatest = curr_val
        idx -= 1
    return result

print(find_left_peaks([1, 2, 5, 3, 1, 2])) # => [5, 3, 2])
print(find_left_peaks([3, 2, 1])) # => [3, 2, 1])
 
