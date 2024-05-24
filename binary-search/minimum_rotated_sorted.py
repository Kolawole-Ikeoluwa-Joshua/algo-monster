"""
A sorted array of unique integers was rotated at an unknown pivot. 

For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. 

Find the index of the minimum element in this array.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: the smallest element is 10 and its index is 3.
"""
def find_min_rotated(arr):
    left, right = 0, len(arr)-1
    boundary_index = -1

    while left <= right:
        mid = (left+right)//2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid -1
        else:
            left = mid + 1

    return boundary_index



# time comp: O(log(n))
# space comp: O(1)

# Example usage:
arr = [30, 40, 50, 10, 20]
index = find_min_rotated(arr)
element = arr[index]

if index != -1:
    print(f"The smallest element is {element} and its index is {index}.")
else:
    print("Element is not present in array")