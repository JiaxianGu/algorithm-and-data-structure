def isValid(s):
    stack = []
    lookup = {"(":")", "[":"]", "{":"}"}
    for parenthesis in s:
        if parenthesis in lookup:
            stack.append(parenthesis)
        elif len(stack) == 0 or lookup[stack.pop()] != parenthesis:
            return False
    return len(stack) == 0