def insertion_sort(arr):
    # every element prior to key is lesser
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >=0 and arr[j] > key:
            # keep shifting elements
            arr[j+1] = arr[j]
            j -= 1
        # insert key in correct position
        arr[j+1] = key
        
# Time comp: 0(n^2)
# Space comp: 0(1) - in-place. stable


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
    insertion_sort(arr)
    print(f"Test Case {i}: After sorting:", end=" ")
    print_array(arr)
    print("--------------------------------")