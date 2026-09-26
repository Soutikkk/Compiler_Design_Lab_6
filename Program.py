def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        # If operand, add directly to postfix
        if ch.isalnum():
            postfix += ch

        # If '(', push to stack
        elif ch == '(':
            stack.append(ch)

        # If ')', pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        # If operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                postfix += stack.pop()
            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Input
expression = input("Enter infix expression: ")

# Output
print("Postfix expression:", infix_to_postfix(expression))