'''
Propagate information through a network

A subset of database servers in a grid network received an update that they must replicate to the remaining nodes. Each second, Nodes broadcast updates to their immediate neighbors, north, west, south, and east.

Given an initial state of the nodes with the updated information, determine how many seconds it will take to propagate the update to the entire network.
 

EXAMPLE(S)
If the state of the network at the 0th second is:
[
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
Then it takes 2 seconds to propagate the information. After the 1st second:
[
  [0, 1, 0],
  [1, 1, 1],
  [0, 1, 0]
]
After the 2nd second:
[
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
]
 

FUNCTION SIGNATURE
function broadcastTime(network) {
def broadcastTime(network: list[list[int]]) -> int:

is it always a square grid?

output: how many seconds until all are 1s

q: nodes to process

find all the ones and add the to the q

while q is not empty
  process ALL the nodes (x, y) in the q 1 by 1

  - mark as 1
  - add all neighboring 0s to the q
  increment the second
'''

def broadcastTime(network: list[list[int]]) -> int:
  q = []
  seconds = 0
  initial_ones = findAllOnes(network)
  for r, c in initial_ones:
    q.extend(getNextZeroes(network, r, c))
  
  while len(q) > 0:
    qs = len(q)
    for _ in range(qs):
      node = q.pop(0)
      r, c = node

      if network[r][c] == 1:
        continue

      network[r][c] = 1
      next_zeroes = getNextZeroes(network, r, c)
      q.extend(next_zeroes)
    
    seconds += 1

  return seconds

def getNextZeroes(net, r, c):
  z = []
  dirs = (-1, 0), (0, 1), (1, 0), (0, -1)
  for rr, cc in dirs:
    dr = rr+r 
    dc = cc+c
    if dr < 0 or dr >= len(net):
      continue
    if dc < 0 or dc >= len(net[0]):
      continue
    if net[dr][dc] == 0:
      z.append((dr, dc))
  return z
    
    
def findAllOnes(net):
  ones = []
  for row in range(len(net)):
    for col in range(len(net[0])):
      if net[row][col] == 1:
        ones.append((row, col))

  return ones

net =[
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
] 
# print(getNextZeroes(net, 1, 1))
# print(broadcastTime([
#   [0, 0, 0],
#   [0, 1, 0],
#   [0, 0, 0]
# ]))

network = [
  [1],
  [0],
  [0],
]
print(broadcastTime(network) == 2)

network = [
  [0,0,0],
  [0,1,0],
  [0,0,0],
]
print(broadcastTime(network) == 2)

network = [
  [0,0,0],
  [0,0,0],
  [0,1,0],
]
print(broadcastTime(network) == 3)

network = [
  [1,0,1],
  [0,0,0],
  [0,1,0],
]
print(broadcastTime(network) == 1)

network = [
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0]
]
print(broadcastTime(network) == 4)

network = [
  [0,0,0,0,0],
  [0,1,0,1,0],
  [0,0,0,0,0],
  [0,1,0,1,0],
  [0,0,0,0,0]
]
print(broadcastTime(network) == 2)

network = [
  [1,0,0,0,1],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
print(broadcastTime(network) == 4)

network = [
  [0,0,0],
  [0,0,0],
  [0,0,0],
  [1,0,0],
]
print(broadcastTime(network) == 5)
