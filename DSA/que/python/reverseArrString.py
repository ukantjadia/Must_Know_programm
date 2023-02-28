"""
   Given an array (or string), the task is to reverse the array/string. 
    
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1
    """

def reverse(arr):
    n = len(arr)
    start ,end = 0,n-1
    while( start < end):
        arr[start] , arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def ownReverse(arr):
    return arr.reverse()
        
if __name__ == "__main__":
    arr = [12,13,14,15,16,17]
    print(arr)
    # reverse(arr)
    ownReverse(arr)
    print(arr)