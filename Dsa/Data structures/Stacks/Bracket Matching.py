from StackClass import Stack

brackets1 = "({[]})"
brackets2 = "(())"
brackets3 = "{()]"
brackets4 = "()"
brackets5 = "([])"
brackets6 = "{[()]}"
brackets7 = "(((())))"
brackets8 = "[({})[]]"
brackets9 = "([)]"
brackets10 = "((("
brackets11 = "())"
brackets12 = "{[}"
brackets13 = "]["

def check_bracket_balance(brackets: str):
    bracket_stack = Stack()
    pairs = {")":"(","}":"{","]":"["}
    for i in brackets:
        if i in "({[":
            bracket_stack.push(i)
        elif i in "]})":
            if bracket_stack.is_empty():
                return False
            elif pairs[i] != bracket_stack.peek():
                return False

            bracket_stack.pop()

    if bracket_stack.is_empty():
        return True
    else:
        return False


test = brackets11
result = check_bracket_balance(test)
print(f"{test} is {'balanced' if result else 'not balanced'}")
