# ฟังก์ชันสำหรับคำนวณผลลัพธ์ของ Postfix Expression
def evaluate_postfix(expression):
    stack = []  # ใช้ List เป็น Stack
    
    # วนลูปผ่านแต่ละตัวในนิพจน์
    for char in expression.split():
        # ถ้าเป็นตัวเลข ให้ push ลง Stack
        if char.isdigit():  # ตรวจสอบว่าเป็นตัวเลข
            stack.append(int(char))
        else:
            # ถ้าเป็นตัวดำเนินการ ให้ pop ตัวเลข 2 ตัวจาก Stack
            operand2 = stack.pop()  # ตัวที่อยู่บนสุด
            operand1 = stack.pop()  # ตัวถัดไป
            
            # คำนวณผลลัพธ์ตามตัวดำเนินการ
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2  # ผลลัพธ์เป็น float
            else:
                raise ValueError(f"ไม่รู้จักตัวดำเนินการ: {char}")
            
            # Push ผลลัพธ์กลับลง Stack
            stack.append(result)
    
    # ผลลัพธ์สุดท้ายใน Stack คือตัวเลขที่คำนวณได้
    return stack.pop()


# รับ Postfix Expression จากผู้ใช้งาน
user_input = input("กรอก Postfix Expression (คั่นด้วยช่องว่าง เช่น '5 6 + 3 *'): ")

# เรียกใช้ฟังก์ชันคำนวณและแสดงผลลัพธ์
try:
    result = evaluate_postfix(user_input)
    print(f"ผลลัพธ์ของ Postfix Expression '{user_input}' คือ: {result}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
