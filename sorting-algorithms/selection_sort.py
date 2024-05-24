def selection_sort(arr):
    # find the smallest item from the unsorted pile and
    # swap it to the sorted pile
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# time comp: O(n^2)
# space comp: O(1) - inplace, unstable

# Test cases
test_cases = [
    [1, 2, 3, 4, 5],          # Already sorted array
    [5, 4, 3, 2, 1],          # Reverse sorted array
    [3, 1, 4, 5, 2],          # Random array
    [4, 4, 4, 4, 4],          # All elements the same
    []                        # Empty array
]

# Function to print test cases
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Run test cases through the selection_sort function
for i, arr in enumerate(test_cases, start=1):
    print(f"Test Case {i}: Before sorting:", end=" ")
    print_array(arr)
    selection_sort(arr)
    print(f"Test Case {i}: After sorting:", end=" ")
    print_array(arr)
    print("--------------------------------")
