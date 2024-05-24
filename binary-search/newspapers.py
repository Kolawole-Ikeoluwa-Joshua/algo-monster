def feasible(newspapers_read_times, num_coworkers, limit):
    # time to keep track of the current worker's time spent, 
    # num_workers to keep track of the number of coworkers used
    time, num_workers = 0, 0
    for read_times in newspapers_read_times:
        # check if current time exceeds the given time limit
        if time + read_times > limit:
            time = 0
            num_workers += 1
        time += read_times
    # edge case to check if we needed an extra worker at the end
    if time != 0:
        num_workers += 1
    # check if the number of workers we need is more than what we have
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times, num_coworkers):
    # binary search to find the minimum time required to read all newspapers with the given number of coworkers.
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1

    while low <= high:
        mid = (low + high) //2
        # checks if it's feasible to split the newspapers within that time limit 
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans



"""
Time complexity: O(n log m)

Setting the initial low and high values takes O(n) to find out the maximum value and the sum of newspapers_read_times. 
Then, performing a binary search is O(log m), and the helper function feasible() that is called inside the binary search loop is O(n). 
Overall, the binary search process takes O(n log m), which is more significant than O(n), thus the time complexity of our solution is O(n log m).

Space Complexity: O(1)
"""

# Test cases
test_cases = [
    ([2, 3, 2, 1, 4], 2),  # Test case 1, Expected ans = 9
    ([7, 2, 5, 10, 8], 2),   # Test case 2, Expected ans = 18
    ([5, 5, 5, 5, 5], 3)    # Test case 3, Expected ans = 10
]

for i, (times, coworkers) in enumerate(test_cases):
    print(f"Test case {i+1}: Newspapers read times: {times}, Number of coworkers: {coworkers}")
    print("Minimum time required:", newspapers_split(times, coworkers))
    print()