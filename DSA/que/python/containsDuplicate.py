"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def duplicate(arr):
    size = len(arr)
    print(size)
    arr = sorted(arr)
    for i in range(1,size):
        if arr[i-1] == arr[i]:
            return True
        
    return False

def duplicate2(arr):
    for i in range(len(arr)):
        if arr[i] in arr:
            return True
    return False

def duplicate3(arr):
    return len(set(arr)) != len(arr)


if __name__ == "__main__":
    arr = [1,1,1,3,3,4,3,2,4,2] 
    arr1 = [1,2,3,4] 
    arr2 = [1,2,3,1] 
    arr3 = [3,3]
    # print(duplicate(arr))
    # print(duplicate2(arr3))
    print(duplicate3(arr)) 