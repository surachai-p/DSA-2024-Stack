class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

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
        
# สร้าง Stack
my_stack = Stack()

# Push ข้อมูล 5 ตัว
for i in range(1, 5):
    my_stack.push(i)

# แสดงข้อมูลบนสุด
print("ข้อมูลบนสุด:", my_stack.peek())

# Pop ข้อมูลออก 3 ตัว
for _ in range(3):
    my_stack.pop()

# แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลที่เหลือ:", my_stack.items)


