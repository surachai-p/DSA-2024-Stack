# การจัดการ Stack ด้วย Python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

# สร้าง Stack และทดสอบการทำงาน
stack = Stack()

# Push ข้อมูล 5 ตัว
data_to_push = [10, 20, 30, 40, 50]
for data in data_to_push:
    stack.push(data)

print("Stack หลังจาก push:", stack.display())

# แสดงข้อมูลบนสุดด้วย peek
print("ข้อมูลบนสุดใน Stack (peek):", stack.peek())

# Pop ข้อมูลออก 3 ตัว
for _ in range(3):
    print("Pop:", stack.pop())

# แสดงข้อมูลที่เหลือใน Stack
print("Stack ที่เหลืออยู่:", stack.display())
