

def reverse_array(arr):
    return arr.reverse()

# In place reversing
def reverse_array_v1(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# Returns a reversed copy of arr
def reverse_array_v2(arr):
    if len(arr) < 2:
        return arr

    return [arr[len(arr) - 1]] + reverse_array_v2(arr[1:(len(arr) - 1)]) + [arr[0]]
