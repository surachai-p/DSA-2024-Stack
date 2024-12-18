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

    def is_empty(self):
        return len(self.items) == 0


def evaluate_postfix(expression):
    """คำนวณผลลัพธ์ของ Postfix Expression"""
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():  # ถ้าเป็นตัวเลข ให้ push ลง Stack
            stack.push(int(token))
        elif token in operators:  # ถ้าเป็นโอเปอเรเตอร์
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                raise ValueError("Invalid Postfix Expression")

            # คำนวณตามโอเปอเรเตอร์
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero")
                result = operand1 / operand2

            stack.push(result)
        else:
            raise ValueError(f"Invalid token: {token}")

    # ผลลัพธ์สุดท้ายใน Stack
    if stack.is_empty() or len(stack.items) > 1:
        raise ValueError("Invalid Postfix Expression")
    return stack.pop()


# รับ Postfix Expression จากผู้ใช้
postfix_expression = input("กรุณาป้อน Postfix Expression (เช่น '3 4 + 2 *'): ")

try:
    result = evaluate_postfix(postfix_expression)
    print(f"ผลลัพธ์ของ Postfix Expression '{postfix_expression}' คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
