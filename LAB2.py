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

    def display(self):
        return self.items


def decimal_to_base(decimal_number, base):
    """แปลงเลขฐาน 10 ให้เป็นฐานที่กำหนด (ฐาน 2 หรือฐาน 16) โดยใช้ Stack"""
    if decimal_number == 0:
        return "0"

    stack = Stack()
    digits = "0123456789ABCDEF"

    # ดำเนินการแปลงเลขฐาน
    while decimal_number > 0:
        remainder = decimal_number % base
        stack.push(digits[remainder])  
        # เก็บตัวเลขหรืออักษรที่เหลือเศษ
        decimal_number //= base

    # สร้างผลลัพธ์จาก Stack
    converted_number = ""
    while not stack.is_empty():
        converted_number += stack.pop()

    return converted_number


# รับค่าจากผู้ใช้
decimal_number = int(input("กรุณาป้อนเลขฐาน 10: "))

# แปลงเป็นฐาน 2
binary_result = decimal_to_base(decimal_number, 2)
print(f"เลขฐาน 2: {binary_result}")

# แปลงเป็นฐาน 16
hex_result = decimal_to_base(decimal_number, 16)
print(f"เลขฐาน 16: {hex_result}")
