"""
A mountain array is defined as an array that

has at least 3 elements
has an element with the largest value called "peak", with index k.

The array elements strictly increase from the first element to A[k], 
and then strictly decreases from A[k + 1] to the last element of the array. 
Thus creating a "mountain" of numbers.
That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], 
we need to find the index k. Note that the peak element is neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.
"""

def peak_of_mountain_array(arr):
    # edge case, Array should have at least 3 elements to form a mountain
    if len(arr) < 3:
        return -1
    
    left, right = 0, len(arr)-1
    peak = -1

    while left <= right:
        mid = (left + right) // 2

        if mid == len(arr)-1 or arr[mid] > arr[mid+1]:
            peak = mid
            right = mid - 1
        else:
            left = mid + 1
    return peak if peak != -1 else -1    # Handle case where peak doesn't exist


# time comp: O(log(n))
# space comp: O(1)

# Example usage:
arr = [0, 1, 2, 3, 2, 1, 0]
index = peak_of_mountain_array(arr)
element = arr[index]

if index != -1:
    print(f"The peak element is {element} and its index is {index}.")
else:
    print("Element is not present in array")