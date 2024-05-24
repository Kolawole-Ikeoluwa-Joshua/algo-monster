def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


"""
Time Complexity:

Best Case: O(n log n) - Occurs when the partition process always picks the middle element as the pivot.

Worst Case: O(n^2) - Occurs when the partition process always picks the greatest or smallest element as the pivot.

Average Case: O(n log n) - On average, it makes O(log n) partitions and each partition requires O(n) comparisons.


Space Complexity: O(log n) - On average, quicksort uses O(log n) stack space for recursion. 
In the worst case, it can require up to O(n) stack space. 

Not stable
"""


# Test cases
test_cases = [
    [1, 2, 3, 4, 5],          # Already sorted array
    [5, 4, 3, 2, 1],          # Reverse sorted array
    [3, 1, 4, 5, 2],          # Random array
    [4, 4, 4, 4, 4],          # All elements the same
    [100, 3, 10, 5, 34, 45, 20],                        
    []                          # Empty array
]

# Function to print test cases
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Run test cases through the quick_sort function
for i, arr in enumerate(test_cases, start=1):
    print(f"Test Case {i}: Before sorting:", end=" ")
    print_array(arr)
    quick_sort(arr, 0, len(arr)-1)
    print(f"Test Case {i}: After sorting:", end=" ")
    print_array(arr)
    print("--------------------------------")