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

# ฟังก์ชันกลับลำดับตัวอักษร
def reverse_string(input_string):
    stack = Stack()
    
    # เพิ่มแต่ละตัวอักษรเข้า stack
    for char in input_string:
        stack.push(char)
    
    # นำตัวอักษรออกจาก stack และสร้างข้อความใหม่ที่กลับลำดับ
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# รับข้อความจากผู้ใช้งาน
input_string = input("กรุณากรอกข้อความที่ต้องการกลับลำดับ: ")

# เรียกใช้ฟังก์ชันและแสดงผล
reversed_string = reverse_string(input_string)
print("ข้อความที่กลับลำดับ:", reversed_string)
