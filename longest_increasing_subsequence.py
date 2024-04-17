'''
/ *
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️
Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q.Given
a
non - empty
array
of
integers, find
its
longest
increasing
subsequence.

Note:
• A
subsequence
of
an
array is a
set
of
numbers
that
aren
't necessarily adjacent in the array but in the same order as they appear.

Examples:
• Given
an
array: [2, 3, -1] // returns[2, 3]
• Given
an
array: [99, 1, 3, 4, 5, 100] // returns[1, 3, 4, 5, 100]

dp = [1, 1, 2, 3, 4, 5]

[3, 6, -23, 10, 8, 1, 3, 15, 6, 9, 55]
[1, 2, 1, 3, 3, ]
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁

at
each
index, look
through
all
prior
values
if val at index is smaller than prior,
check
all
prior
indexes
for smaller values(binary search opportunity?)
if one of them is smaller, set max = that value + 1

[1, 3, 4, 5, 99, 100] - values
[1, 2, 3, 4, 0, 5] - indices

look
at
current
value in sequence
binary
search
for value greater than it in our sorted values list where idx > curr idx

🟨 Javascript
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
function
longestIncreasingSubsequence(array)
{
// Write
your
code
here.
return []
}

const
dp = [1]

at
a
given
index,
value is either
index + val(rest
of
array)
or index + 1 + val(rest
of
array)
* /
// function
longestIncreasingSubsequence(array)
{
// let
max = 1
// for (let j = 0; j < array.length; j++) {
                                          // let count = 1
// let v = array[j]
// for (let i = j + 1; i < array.length; i++) {
// console.log('v: ', v, '| array[i]:', array[i])
// if (v < array[i]) {
// count++
//}
// // console.log('count:', count)
//}
// max = Math.max(max, count)
// console.log('max:', max)
//}
// console.log(max)
// return max
//}

// at
each
index, look
through
all
prior
values
// if val
at
index is smaller
than
prior,
// check
all
prior
indexes
for smaller values(binary search opportunity ?)
// if one of them is smaller, set max = that value + 1
// function longestIncreasingSubsequence(array) {
// [99, 1, 3, 4, 5, 100]
// i
// dp = [1, 1, 2, 3, ]
function
longestIncreasingSubsequence(array)
{
    const
dp = [1]

for (let i = 1; i < array.length; i++) {
    dp[i] = 1;
for (let j = 0; j < i; j++) {
const priorNumber = array[j]
if (priorNumber < array[i]) {
dp[i] = Math.max(dp[i], dp[j] + 1)
}
}
}
return Math.max(...
dp)
}
console.log(longestIncreasingSubsequence([0]) == = 1)
console.log(longestIncreasingSubsequence([2, 3, -1]) == = 2)
console.log(longestIncreasingSubsequence([99, 1, 3, 4, 5, 100]) == = 5)
console.log(longestIncreasingSubsequence([3, 6, -23, 10, 8, 1, 3, 15, 6, 9, 55]) == = 6)
'''