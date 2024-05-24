"""
Given an integer, 
find its square root without using the built-in square root function. 
Only return the integer part (truncate the decimals).
"""

def square_root(n):
    if n == 0:
        return 0
    left, right = 1, n
    res = -1

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid
        elif mid * mid > n:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res - 1

# time comp: O(log(n))
# space comp: O(1)


# Example usage:
def test_square_root():
    # Test case 1: Perfect square
    assert square_root(16) == 4

    # Test case 2: Non-perfect square
    assert square_root(10) == 3  # Floor value of square root of 10 is 3

    # Test case 3: Edge case - 0
    assert square_root(0) == 0

    # Test case 4: Large value
    assert square_root(1000000) == 1000

    # Test case 6: Large non-perfect square
    assert square_root(999999) == 999

    print("All test cases pass!")

# Run the test cases
test_square_root()
