'''
Define a chain of a list L as a sequence of elements from L, not necessarily contiguous, that are arranged in ascending order in L. For instance, chains in the list `[1, 3, 2, 4]` include `[1]`, `[1, 3]`, `[1, 3, 4]`, `[1, 2, 4]`, and `[1, 4]`.

Given an input list, the goal is to compute the length of its longest chain. List elements are guaranteed to be unique. Examples:

```
getLengthOfLongestChain([1, 2, 3, 4]) -> 4  // [1, 2, 3, 4]
getLengthOfLongestChain([4, 3, 2, 1]) -> 1  // [1], [2], [3], or [4]
getLengthOfLongestChain([1, 3, 2, 4]) -> 3  // [1, 3, 4] or [1, 2, 4]
getLengthOfLongestChain([1, 3, 2, 4, 5, 8, 6, 7]) -> 6  // [1, 2, 4, 5, 6, 7]
getLengthOfLongestChain([10, 2, 7, 3, 6, 1, 4, 5]) -> 4  // [2, 3, 4, 5]
```

Note: This problem can be solved with Dynamic Programming or Backtracking. Here we're intending the backtracking version.
'''

def getLengthOfLongestChain(arr):
    chain_set = set()
    def helper(start, curr_chain):
        nonlocal max_chain
        chain_set.add(tuple(curr_chain))
        max_chain = max(max_chain, len(curr_chain))
        for i in range(start, len(arr)):
            if not curr_chain or curr_chain[-1] < arr[i]:
                curr_chain.append(arr[i])
                helper(i + 1, curr_chain)
                curr_chain.pop()

    
    max_chain = 0
    helper(0, [])
    print(list(chain_set))
    return max_chain

print(getLengthOfLongestChain([1,2,3,4])) # -> 4 // [1,2,3,4]
# print(getLengthOfLongestChain([4, 3, 2, 1])) # -> 1  // [1], [2], [3], or [4]
# print(getLengthOfLongestChain([1, 3, 2, 4])) # -> 3  // [1, 3, 4] or [1, 2, 4]
# print(getLengthOfLongestChain([1, 3, 2, 4, 5, 8, 6, 7])) # -> 6  // [1, 2, 4, 5, 6, 7]
# print(getLengthOfLongestChain([10, 2, 7, 3, 6, 1, 4, 5])) # -> 4  // [2, 3, 4, 5]

