def merge_sort(arr):
    """
    Merge sort is a divide-and-conquer algorithm that divides the unsorted list into N sublists, 
    each containing one element (a list of one element is considered sorted). 
    Then repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining, 
    which will be the sorted list.
    
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# time comp: O(n log n) - in all cases
# space comp: O(n) - due to extra arrays used in merge process


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
    merge_sort(arr)
    print(f"Test Case {i}: After sorting:", end=" ")
    print_array(arr)
    print("--------------------------------")