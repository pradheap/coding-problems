
def encode(word):
    result = ''
    count = 0
    prev = ''

    for ch in word:
        if prev == ch:
            count += 1
        else:
            if count > 0:
                result += prev + str(count)
            count = 1
        prev = ch

    if count > 0:
        result += prev + str(count)
    return result
