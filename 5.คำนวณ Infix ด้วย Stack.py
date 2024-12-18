def precedence(op):
    """ฟังก์ชันคืนค่าลำดับความสำคัญของตัวดำเนินการ"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_operation(a, b, op):
    """ฟังก์ชันสำหรับคำนวณผลลัพธ์ของ a op b"""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    raise ValueError(f"ตัวดำเนินการ {op} ไม่รองรับ")

def evaluate_infix(expression):
    """ฟังก์ชันประเมินผลนิพจน์ Infix โดยใช้ Stack"""
    operand_stack = []  # สำหรับตัวเลข
    operator_stack = []  # สำหรับตัวดำเนินการ

    i = 0
    while i < len(expression):
        char = expression[i]

        # ถ้าคือช่องว่าง ให้ข้ามไป
        if char == ' ':
            i += 1
            continue

        # ถ้าคือเลข ให้ push ลง operand_stack
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operand_stack.append(num)
            continue  # ไม่ต้องเพิ่ม i เพิ่มอีกเพราะ while-loop เลื่อนไปแล้ว

        # ถ้าคือวงเล็บเปิด '(' ให้ push ลง operator_stack
        if char == '(':
            operator_stack.append(char)

        # ถ้าคือวงเล็บปิด ')' ให้คำนวณจนกว่าจะเจอ '('
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                op = operator_stack.pop()
                b = operand_stack.pop()
                a = operand_stack.pop()
                operand_stack.append(apply_operation(a, b, op))
            operator_stack.pop()  # เอา '(' ออกจาก stack

        # ถ้าเป็นตัวดำเนินการ
        elif char in '+-*/':
            # จัดการลำดับความสำคัญของตัวดำเนินการ
            while (operator_stack and 
                   precedence(operator_stack[-1]) >= precedence(char)):
                op = operator_stack.pop()
                b = operand_stack.pop()
                a = operand_stack.pop()
                operand_stack.append(apply_operation(a, b, op))
            operator_stack.append(char)

        i += 1

    # คำนวณตัวดำเนินการที่เหลือใน stack
    while operator_stack:
        op = operator_stack.pop()
        b = operand_stack.pop()
        a = operand_stack.pop()
        operand_stack.append(apply_operation(a, b, op))

    # ผลลัพธ์สุดท้ายใน operand_stack
    return operand_stack.pop()


# รับ Infix Expression จากผู้ใช้งาน
user_input = input("กรอก Infix Expression (เช่น 3 + 5 * (2 - 8)): ")

# เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
try:
    result = evaluate_infix(user_input)
    print(f"ผลลัพธ์ของ Infix Expression '{user_input}' คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
