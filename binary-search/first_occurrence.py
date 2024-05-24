"""
Given a sorted array of integers and a target integer, 
find the first occurrence of the target and return its index. 
Return -1 if the target is not in the array.
"""
def first_occurrence(arr, target):
    l, r = 0, len(arr)-1
    ans = -1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == target:
            ans = mid
            r = mid -1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans

# time comp: O(log(n))
# space comp: O(1)


# Example usage:
array = [1, 2, 2, 2, 3, 4, 5, 6]
target = 2
index = first_occurrence(array, target)
if index != -1:
    print("Index of the first occurrence of target:", index)
else:
    print("No True value found in the array.")