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
    
    # แสดงข้อมูลทั้งหมดใน stack
    def display(self):
        return self.stack

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 2
def decimal_to_binary(n):
    stack = Stack()
    
    # แบ่ง n ด้วย 2 และเก็บเศษใน stack
    while n > 0:
        stack.push(n % 2)
        n = n // 2
    
    # นำข้อมูลใน stack ออกและสร้างเลขฐาน 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return binary if binary else "0"

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 16
def decimal_to_hexadecimal(n):
    stack = Stack()
    hex_digits = "0123456789ABCDEF"  # ตัวเลขในฐาน 16
    
    # แบ่ง n ด้วย 16 และเก็บเศษใน stack
    while n > 0:
        stack.push(hex_digits[n % 16])
        n = n // 16
    
    # นำข้อมูลใน stack ออกและสร้างเลขฐาน 16
    hexadecimal = ""
    while not stack.is_empty():
        hexadecimal += str(stack.pop())
    
    return hexadecimal if hexadecimal else "0"

# รับค่าจากผู้ใช้งาน
decimal_number = int(input("กรุณากรอกเลขฐาน 10: "))

# แปลงเป็นฐาน 2 และฐาน 16
binary = decimal_to_binary(decimal_number)
hexadecimal = decimal_to_hexadecimal(decimal_number)

# แสดงผล
print(f"เลขฐาน 10 {decimal_number} เป็นเลขฐาน 2: {binary}")
print(f"เลขฐาน 10 {decimal_number} เป็นเลขฐาน 16: {hexadecimal}")
