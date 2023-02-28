"""
Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
                Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
                Maximum element is: 35*/
                
"""


class couple:
    
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr):
    n = len(arr)
    print(n)
    minmax = couple() 

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    elif n == 2:
        # for more than on value in arr
        if arr[0] > arr[1]:
            minmax.min = arr[1]
            minmax.max = arr[0]
        else:
            minmax.min = arr[0]
            minmax.max = arr[1]
        return minmax
    else:
        for i in range(0,n):
            if arr[i] > minmax.max:
                minmax.max = arr[i]
            elif arr[i] < minmax.min:
                minmax.min = arr[i]

            return minmax

def withInBuilt(arr):
    n = len(arr)
    minmax = couple()
    if n == 0:
        print("List is EMPTY!! ")
        return minmax
    else:
        arr = sorted(arr)
        minmax.min = arr[0]
        minmax.max = arr[-1]
        return minmax



# driver code

if __name__ == "__main__":
    arr1 = [12,23,45,232,341,1,2,5,3]
    arr2 = [0,1]
    arr3 = [2]
    arr4 = []
    minmax = getMinMax(arr1)
    # minmax = withInBuilt(arr4)
    print(f"Maximum element is: {minmax.max}")
    print(f"Minimum element is: {minmax.min}")