# Majority element is the one that occurs n/2 times in a list 
# of n elements.
# Moore's voting algo
def majority_element(arr):
    if arr is None:
        return arr

    majority_el = None
    count = 0

    for el in arr:
        if count == 0:
            majority_el = el
            count = 1
        elif el == majority_el:
            count += 1
        else:
            count -= 1
    
    if majority_el is not None:
        majority_count = 0
        for el in arr:
            if el == majority_el:
                majority_count += 1
        
        if majority_count <= (len(arr)/2):
            majority_el = None

    return majority_el

# O(NLog(N)) Solution using sorting
def majority_element_v1(arr):
    if arr is None or len(arr) == 0:
        return None

    size = len(arr)
    arr.sort()
    majority_element = arr[(size // 2)]
    majority_count = 0
    for el in arr:
        if el == majority_element:
            majority_count += 1

    if majority_count <= (len(arr) / 2):
        majority_element = None

    return majority_element


