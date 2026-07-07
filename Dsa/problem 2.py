def check_balance(bracket_string):
    stack = []
    pairs = { "(": ")","[": "]","{": "}"}
    for bracket in bracket_string:
        if bracket in pairs:
            stack.append(bracket)
        elif bracket in pairs.values():
            if not stack:
                return False
            top = stack.pop()
            if pairs[top] != bracket:
                return False
    return len(stack) == 0

print(check_balance("()"))        # True
print(check_balance("(()())"))    # True
print(check_balance("{[()]}"))    # True

print(check_balance("("))         # False
print(check_balance("(()"))       # False
print(check_balance("([)]"))      # False
print(check_balance(")("))        # False
print(check_balance("]"))         # False