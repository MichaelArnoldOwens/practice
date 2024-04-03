'''
Question :

(USE RECURSIVE APPROACH)

Q : Given an integer array and an integer, find whether the integer exists in the array. Return a boolean.

Input : arr = [1,2,3,4,5], num = 5
Output : True


Input : arr = [1,2,3,4,5], num = 6
Q : Given an integer array and an integer, return how many times the integer exists in the array.

Q : Reverse the values in an array
Input : [1,2,3,4]
Output : [4,3,2,1]

'''
def reverse(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse(arr, left + 1, right - 1)

def reverse_arr(arr):
   if len(arr) <= 1:
       return arr
   return reverse(arr, 0, len(arr) - 1)

print(reverse_arr([5,4,3,2,1]))

def count(arr, target, i = 0):
    if i >= len(arr):
        return 0
    if arr[i] == target:
        return 1 + count(arr, target, i + 1)
    else:
        return count(arr, target, i + 1)

def count_instances(arr, target):
    return count(arr, target)

print(count_instances([1,2,3,4,5,2,2,2,2], 2))


# linear search
def walk(arr, target, i = 0):
    if i >= len(arr):
        return False
    if arr[i] == target:
        return True

    return walk(arr, target, i + 1)

def recursive_find(arr, target):
    return walk(arr, target)

arr = [1, 2, 3, 4, 5]
target = 5

print(recursive_find(arr, target))
