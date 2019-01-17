
# O(N^2) solution.
def indices_for_two_sum(arr, sum):
    if len(arr) < 2:
        return None
    
    for idx1 in range(len(arr) - 1):
        for idx2 in range(idx1 + 1, len(arr)):
            if (arr[idx1] + arr[idx2]) == sum:
                return (idx1, idx2)
    
    return None

# O(N) solution.
# Two pointer solution
def indices_for_two_sum_v1(arr, sum):
    if len(arr) < 2:
        return None
    
    left = 0
    right = len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == sum:
            return (left, right)
        elif curr_sum < sum:
            left += 1
        else:
            right -= 1
    
    return None
