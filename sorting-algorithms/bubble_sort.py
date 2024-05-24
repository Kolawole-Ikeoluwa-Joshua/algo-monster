def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # compare each adjacent element, such that in each iteration
        # the largest element goes to the end of the array
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break



# Time comp: O(n^2) average or worst case/ O(n) best case if array is already sorted 
# Space comp: O(1) - inplace


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

# Run test cases through the selection_sort function
for i, arr in enumerate(test_cases, start=1):
    print(f"Test Case {i}: Before sorting:", end=" ")
    print_array(arr)
    bubble_sort(arr)
    print(f"Test Case {i}: After sorting:", end=" ")
    print_array(arr)
    print("--------------------------------")