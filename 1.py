class Stack:
    def __init__(self):
        self.stack = []
    
    # เพิ่มข้อมูลเข้า stack
    def push(self, item):
        self.stack.append(item)
    
    # ดูข้อมูลบนสุดของ stack โดยไม่ลบ
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
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

# สร้าง Stack
stack = Stack()

# ทดสอบการ push ข้อมูล 5 ตัว
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# แสดงข้อมูลบนสุด
print("ข้อมูลบนสุดของ Stack (Peek):", stack.peek())

# ทดสอบการ pop ข้อมูลออก 3 ตัว
print("Pop ข้อมูลออก:", stack.pop())
print("Pop ข้อมูลออก:", stack.pop())
print("Pop ข้อมูลออก:", stack.pop())

# แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลที่เหลือใน Stack:", stack.display())
