class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def precedence(op):
    """ลำดับความสำคัญของโอเปอเรเตอร์"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_operator(a, b, operator):
    """คำนวณผลลัพธ์จากโอเปอเรเตอร์และอาร์กิวเมนต์"""
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    raise ValueError(f"Unsupported operator: {operator}")


def infix_to_postfix(expression):
    """แปลง Infix Expression เป็น Postfix Expression"""
    stack = Stack()
    postfix = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # ตัวเลข
            postfix.append(token)
        elif token in "+-*/":  # โอเปอเรเตอร์
            while (not stack.is_empty() and
                   precedence(stack.peek()) >= precedence(token)):
                postfix.append(stack.pop())
            stack.push(token)
        elif token == '(':  # วงเล็บเปิด
            stack.push(token)
        elif token == ')':  # วงเล็บปิด
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # เอา '(' ออก

    # ดึงโอเปอเรเตอร์ที่เหลือใน Stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)


def evaluate_postfix(postfix):
    """คำนวณผลลัพธ์จาก Postfix Expression"""
    stack = Stack()
    tokens = postfix.split()

    for token in tokens:
        if token.isdigit():  # ตัวเลข
            stack.push(int(token))
        elif token in "+-*/":  # โอเปอเรเตอร์
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.push(result)

    return stack.pop()


def evaluate_infix(expression):
    """คำนวณผลลัพธ์ของ Infix Expression"""
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


# รับ Infix Expression จากผู้ใช้
infix_expression = input("กรุณาป้อน Infix Expression (เช่น '3 + 5 * ( 2 - 8 )'): ")

try:
    result = evaluate_infix(infix_expression)
    print(f"ผลลัพธ์ของ Infix Expression '{infix_expression}' คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
