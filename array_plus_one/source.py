
def plus_one(arr):
    if len(arr) == 0:
        return arr
    
    # Add 1 to the LSB which is the tail end of the list.
    arr[len(arr) - 1] = arr[len(arr) - 1] + 1

    to_carry = 0
    # Traverse the list from LSB to MSB, from tail to head.
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = arr[i] + to_carry
        if arr[i] > 9:
            arr[i] %= 10
            to_carry = 1
        else:
            # Short circuit and return the arr, if the arr[i] 
            # is lesser than or equal to 9
            return arr
        
    arr = [1] + arr
    
    return arr
