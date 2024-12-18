class Stack:
    def __init__(self):
        self.stack = []

    # เพิ่มข้อมูลเข้า stack
    def push(self, item):
        self.stack.append(item)

    # ลบข้อมูลบนสุดของ stack และส่งค่าที่ลบออก
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    # ตรวจสอบว่า stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0

# ฟังก์ชันคำนวณผลลัพธ์จาก Postfix Expression
def evaluate_postfix(expression):
    stack = Stack()
    
    # แยก expression โดยใช้ช่องว่างเป็นตัวแบ่ง
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # ถ้าเป็นตัวเลข
            stack.push(int(token))  # นำเข้า stack
        else:  # ถ้าเป็นตัวดำเนินการ
            operand2 = stack.pop()  # ค่าแรก
            operand1 = stack.pop()  # ค่าที่สอง
            
            # คำนวณผลลัพธ์ตามตัวดำเนินการ
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                raise ValueError(f"ตัวดำเนินการ '{token}' ไม่ถูกต้อง")
            
            stack.push(result)  # ใส่ผลลัพธ์กลับเข้า stack
    
    # ผลลัพธ์สุดท้ายจะอยู่ที่บนสุดของ stack
    return stack.pop()

# รับข้อมูลจากผู้ใช้
postfix_expression = input("กรุณากรอกนิพจน์ Postfix (ตัวดำเนินการและตัวเลขคั่นด้วยช่องว่าง): ")

# คำนวณผลลัพธ์ของนิพจน์ Postfix
try:
    result = evaluate_postfix(postfix_expression)
    print(f"ผลลัพธ์ของนิพจน์ Postfix คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
