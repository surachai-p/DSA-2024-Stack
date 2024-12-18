class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# ฟังก์ชันแปลง Infix เป็น Postfix
def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # ถ้าคือเลข (operand)
        if char.isdigit():
            postfix.append(char)
        
        # ถ้าคือเครื่องหมายดำเนินการ
        elif char in '+-*/':
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(char)):
                postfix.append(stack.pop())
            stack.push(char)
        
        # ถ้าเจอเครื่องหมาย '('
        elif char == '(':
            stack.push(char)
        
        # ถ้าเจอเครื่องหมาย ')'
        elif char == ')':
            while stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # ลบ '(' ออกจาก stack
        
        i += 1

    # หลังจากวน loop เสร็จ ให้เอาทุกตัวที่เหลือใน stack ออกมา
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return "".join(postfix)

# ฟังก์ชันคำนวณ Postfix Expression
def evaluate_postfix(postfix):
    stack = Stack()
    
    for char in postfix:
        # ถ้าเป็นตัวเลข
        if char.isdigit():
            stack.push(int(char))
        
        # ถ้าเป็นตัวดำเนินการ
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.push(result)
    
    return stack.pop()


def calculate_infix(expression):
    postfix = infix_to_postfix(expression)
    print(f"Postfix Expression: {postfix}")
    result = evaluate_postfix(postfix)
    return result


expression = input("กรุณากรอก Infix Expression (เช่น 3 + 5 * (2 - 8)): ")


try:
    result = calculate_infix(expression)
    print(f"ผลลัพธ์ของนิพจน์ Infix คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
