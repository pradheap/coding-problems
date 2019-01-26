
def square(arr):
    result = [None] * len(arr)
    left = 0
    right = len(arr) - 1
    target = len(result) - 1

    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        if left_sq > right_sq:
            result[target] = left_sq
            left += 1
        else:
            result[target] = right_sq
            right -= 1
        target -= 1
    
    return result
