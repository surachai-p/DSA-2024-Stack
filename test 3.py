class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def is_operator(c):
    return c in ['+', '-', '*', '/']

def precedence(c):
    if c in ('+', '-'):
        return 1
    elif c in ('*', '/'):
        return 2
    return -1

def infix_to_postfix(infix):
    output = ''
    stack = Stack()
    for c in infix:
        if c.isalnum():
            output += c
        elif c == '(':
            stack.push('(')
        elif c == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while not stack.is_empty() and precedence(c) <= precedence(stack.peek()):
                output += stack.pop()
            stack.push(c)
    while not stack.is_empty():
        output += stack.pop()
    return output

def evaluate_postfix(exp):
    stack = Stack()
    for i in exp:
        if i.isdigit():
            stack.push(int(i))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if i == '+':
                stack.push(val2 + val1)
            elif i == '-':
                stack.push(val2 - val1)
            elif i == '*':
                stack.push(val2 * val1)
            elif i == '/':
                stack.push(val2 // val1)
    return stack.pop()

def main():
    while True:
        infix_expression = input("Enter infix expression (or 'q' to quit): ")
        if infix_expression == 'q':
            break
        postfix_expression = infix_to_postfix(infix_expression)
        result = evaluate_postfix(postfix_expression)
        print("Postfix expression:", postfix_expression)
        print("Result:", result)

if __name__ == "__main__":
    main()