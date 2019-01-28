
# Assumption no duplicates in the given sorted array
# O(N) solution
def get_position(arr, target):
    index = -1

    for i in range(len(arr)):
        if target > arr[i]:
            index = i
        else:
            break

    return index + 1
