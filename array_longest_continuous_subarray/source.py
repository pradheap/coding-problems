
def subarray(arr):
    res = 0
    if len(arr) < 1:
        return res

    prev = arr[0]
    lcs = 1
    for i in arr[1:]:
        if prev < i:
            lcs += 1
            res = max(res, lcs)
        else:
            lcs = 1
        prev = i

    return max(res, lcs)
