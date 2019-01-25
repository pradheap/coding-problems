from collections import Counter

# Also same as is anagram
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    # O(NLg(N)) solution
    # return sorted(s1) == sorted(s2)

    # O(N) in runtime and constant space complexity if ascii only
    counter = Counter()
    for c in s1:
        counter[c] += 1
    
    for c in s2:
        counter[c] -= 1
    
    # Counter is a dict subclass, so we have an 
    # extended api on top of the actual dict api.
    for i in counter.values():
        if i != 0:
            return False
    
    return True
