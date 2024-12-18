# สร้าง class Stack
class Stack:
    def __init__(self):
        self.stack = []

    # Method สำหรับ push ข้อมูลลง Stack
    def push(self, item):
        self.stack.append(item)

    # Method สำหรับ pop ข้อมูลออกจาก Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    # Method สำหรับตรวจสอบว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0


# ฟังก์ชันสำหรับกลับลำดับตัวอักษรโดยใช้ Stack
def reverse_string_with_stack(input_string):
    stack = Stack()
    
    # Push ตัวอักษรทั้งหมดลง Stack
    for char in input_string:
        stack.push(char)

    # Pop ตัวอักษรออกจาก Stack เพื่อกลับลำดับ
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# รับข้อความจากผู้ใช้งาน
user_input = input("กรอกข้อความที่ต้องการกลับลำดับ: ")

# เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
reversed_output = reverse_string_with_stack(user_input)
print("ข้อความที่กลับลำดับ:", reversed_output)
