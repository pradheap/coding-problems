# Given a parentheses string, return the minimum number of
# parentheses we must add to make the resulting string valid.
def minimum_add(s):
    st = []
    min_add = 0
    for ch in s:
        if ch == '(':
            st.append(ch)
        elif ch == ')':
            if len(st) == 0:
                min_add += 1
            else:
                st.pop()

    min_add += len(st)
    return min_add
