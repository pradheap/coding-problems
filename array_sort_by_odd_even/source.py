
def sort_by_parity(arr):
    if len(arr) < 2:
        return arr
    
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0 and arr[right] % 2 > 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] % 2 > 0:
            left += 1
        if arr[right] % 2 == 0:
            right -= 1
