'''
❓ PROMPT
We have a triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

Example(s)
triangle(2) == 3
triangle(3) == 6
triangle(5) == 15
 

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
function triangle(rows) {
def triangle(rows: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def triangle(rows: int) -> int:
  if rows <= 0:
    return 0
  return rows + triangle(rows - 1)

print(triangle(2) == 3)
print(triangle(3) == 6)
print(triangle(5) == 15)
 
