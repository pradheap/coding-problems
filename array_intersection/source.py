# Given two arrays, write a function to compute their intersection.

# Note:

# Each element in the result must be unique.
# The result can be in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Solution without using in-built functions, Otherwise it's
# just one-line solution in Python list(set(arr1)&set(arr2))
# O(M * N) solution
def find_intersection(arr1, arr2):
    if arr1 is None or arr2 is None:
        return []
    
    if len(arr1) == 0 or len(arr2) == 0:
        return []
    
    intersection = []
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2 and elem1 not in intersection:
                intersection.append(elem1)
    
    return intersection

# A slightly optimized solution using sorting.
# O(NlogN) using two pointers on each list.
def find_intersection_v1(arr1, arr2):
    if arr1 is None or arr2 is None:
        return []
    
    if len(arr1) == 0 or len(arr2) == 0:
        return []
    intersection = []
    # Sort
    arr1.sort()
    arr2.sort()

    p1 = 0
    arr1_length = len(arr1)
    p2 = 0
    arr2_length = len(arr2)
    prev = None
    
    while p1 < arr1_length and p2 < arr2_length:
        if arr1[p1] == arr2[p2] and prev != arr1[p1]:
            # Increment p1, p2 when the elements are equal and unique
            intersection.append(arr1[p1])
            prev = arr1[p1]
            p1 += 1
            p2 += 1
        while p1 < arr1_length and arr1[p1] == prev:
            # Increment p1 when the arr1 elements are just dupes.
            p1 += 1
        while p2 < arr2_length and arr2[p2] == prev:
            # Increment p2 when the arr2 elements are just dupes.
            p2 += 1
        while p1 < arr1_length and p2 < arr2_length:
            # Increment p1 when the arr1 elements are lesser than p2 element.
            # Increment p2 when the arr2 elements are lesser than p1 element.
            # Else break and let the first if deal with p1 == p2 elements.
            if arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr1[p1]:
                p2 += 1
            else:
                break

    return intersection
