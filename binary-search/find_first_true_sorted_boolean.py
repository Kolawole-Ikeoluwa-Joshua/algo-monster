def first_true_index(arr):

    left, right = 0, len(arr)-1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


# time comp: O(log(n))
# space comp: O(1)


# Example usage:
boolean_array = [False, False, False, True, True, True, True]
index = first_true_index(boolean_array)
if index != -1:
    print("Index of the first True value:", index)
else:
    print("No True value found in the array.")