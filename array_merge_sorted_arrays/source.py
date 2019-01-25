
def merge(arr1, arr2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1

    while p1 < len(arr1):
        result.append(arr1[p1])
        p1 += 1
    
    while p2 < len(arr2):
        result.append(arr2[p2])
        p2 += 1
    
    return result


def merge_in_place(arr1, arr2):
    p1 = len(arr1) - 1
    p2 = len(arr2) - 1
    p3 = len(arr1) + len(arr2) - 1

    # Just initialize extra space to None.
    for i in range(p3 - p1):
        arr1.append(None)

    # We go from the end of the arr1 to 0 to minimize the number of swaps.
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr1[p3] = arr1[p1]
            p1 -= 1
        else:
            arr1[p3] = arr2[p2]
            p2-= 1

        p3 -= 1
    
    while p2 >= 0:
        arr1[p3] = arr2[p2]
        p2 -= 1
        p3 -= 1
