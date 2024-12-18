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

    # Method สำหรับแสดงข้อมูลใน Stack (ถ้าต้องการ debug)
    def display(self):
        return self.stack


# ฟังก์ชันสำหรับแปลงเลขฐาน 10 เป็นเลขฐาน 2 หรือฐาน 16
def convert_base_with_stack(number, base):
    stack = Stack()
    digits = "0123456789ABCDEF"  # ใช้สำหรับการแปลงเลขฐาน 16

    # ดำเนินการแปลงเลข
    while number > 0:
        remainder = number % base
        stack.push(remainder)  # เก็บเศษไว้ใน Stack
        number //= base

    # สร้างผลลัพธ์จาก Stack
    result = ""
    while not stack.is_empty():
        result += digits[stack.pop()]

    return result


# รับตัวเลขฐาน 10 จากผู้ใช้งาน
decimal_number = int(input("กรอกตัวเลขฐาน 10: "))

# แปลงเลขฐาน 10 เป็นฐาน 2
binary_result = convert_base_with_stack(decimal_number, 2)
print(f"เลขฐาน 2 ของ {decimal_number} คือ: {binary_result}")

# แปลงเลขฐาน 10 เป็นฐาน 16
hex_result = convert_base_with_stack(decimal_number, 16)
