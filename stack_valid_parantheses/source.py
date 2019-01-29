
def is_valid(parantheses):
    if len(parantheses) == 0:
        return False

    stack = []
    for ch in parantheses:
        if ch in ['{', '(', '[']:
            stack.append(ch)
        else:
            opening_char = None
            if len(stack) > 0:
                opening_char = stack.pop()

            if ch == ')' and opening_char != '(':
                return False
            elif ch == ']' and opening_char != '[':
                return False
            elif ch == '}' and opening_char != '{':
                return False

    if len(stack) == 0:
        return True
        
    return False
