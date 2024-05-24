"""
Given an array of integers sorted in increasing order and a target, 
find the index of the first element in the array that is larger than or equal to the target. 
Assume that it is guaranteed to find a satisfying number.

"""

def first_not_smaller(arr, target):
    left, right = 0, len(arr)-1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2

        # feasible(mid) = arr[i] >= target
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_index


# time comp: O(log(n))
# space comp: O(1)


# Example usage:
array = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6

index = first_not_smaller(array, target)
if index != -1:
    print("Index of the first true element:", index)
else:
    print("No True element found in the array.")