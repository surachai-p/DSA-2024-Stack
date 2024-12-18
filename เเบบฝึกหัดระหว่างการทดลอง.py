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
            return "Stack is empty"

    # Method สำหรับดูข้อมูลบนสุดของ Stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Method สำหรับตรวจสอบว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0

    # Method สำหรับแสดงข้อมูลใน Stack ทั้งหมด
    def display(self):
        return self.stack


# สร้าง Stack ใหม่
my_stack = Stack()

# 1. ทดสอบการ push ข้อมูล 5 ตัว
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)

print("หลังการ push ข้อมูล 5 ตัว:", my_stack.display())

# 2. แสดงข้อมูลบนสุดโดยใช้ peek
print("ข้อมูลบนสุดของ Stack (peek):", my_stack.peek())

# 3. ทดสอบ pop ข้อมูลออก 3 ตัว
print("pop:", my_stack.pop())
print("pop:", my_stack.pop())
print("pop:", my_stack.pop())

# 4. แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลที่เหลือใน Stack:", my_stack.display())
