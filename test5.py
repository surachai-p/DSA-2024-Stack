####ส่วนที่ 5: คำนวณ Infix ด้วย Stack
  # ฟังก์ชันที่ใช้ในการประเมินผลนิพจน์ในรูป Infix
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(op, b, a):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

def infix_to_postfix(expression):
    stack = []  # Stack สำหรับตัวดำเนินการ
    output = []  # เก็บผลลัพธ์ที่แปลงจาก Infix เป็น Postfix
    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลข ให้เพิ่มเข้า output
            output.append(char)
        elif char == '(':  # ถ้าเจอวงเล็บเปิด ให้ใส่เข้า stack
            stack.append(char)
        elif char == ')':  # ถ้าเจอวงเล็บปิด ให้ pop จนกว่าจะเจอวงเล็บเปิด
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # ลบวงเล็บเปิด
        else:  # ถ้าเป็นตัวดำเนินการ
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)
    
    # เติมตัวดำเนินการที่เหลือใน stack ลงไปใน output
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลข ให้เพิ่มเข้า stack
            stack.append(int(char))
        else:  # ถ้าเป็นตัวดำเนินการ ให้ pop ตัวเลข 2 ตัวจาก stack แล้วดำเนินการ
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(char, b, a)
            stack.append(result)
    return stack[-1]  # ผลลัพธ์สุดท้ายจะอยู่ใน top ของ stack

def evaluate_infix(expression):
    # แปลงจาก Infix เป็น Postfix
    postfix = infix_to_postfix(expression)
    # คำนวณผลจาก Postfix
    return evaluate_postfix(postfix)

# ทดสอบการทำงาน
expression = input("กรุณากรอกนิพจน์ Infix: ")
result = evaluate_infix(expression)
print(f"ผลลัพธ์ของนิพจน์ Infix '{expression}' คือ: {result}")
