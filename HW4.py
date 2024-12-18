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

# ฟังก์ชันตรวจสอบความถูกต้องของ JSON string
def is_valid_json(json_string):
    stack = Stack()
    # เครื่องหมายเปิดและปิดที่ต้องการตรวจสอบ
    opening = {'{', '[', '(', '"'}
    closing = {'}': '{', ']': '[', ')': '(', '"': '"'}
    
    i = 0
    while i < len(json_string):
        char = json_string[i]
        
        if char in opening:
            # ถ้าเป็นเครื่องหมายเปิด ให้เพิ่มเข้า stack
            stack.push(char)
        elif char in closing:
            # ถ้าเป็นเครื่องหมายปิด ตรวจสอบว่า stack ว่างหรือไม่
            if stack.is_empty():
                return False
            
            # นำค่าจาก stack ออกมาว่าตรงกับเครื่องหมายปิดหรือไม่
            top = stack.pop()
            if closing[char] != top:
                return False
        i += 1
    
    # ถ้า stack ว่างเปล่า หมายความว่าเครื่องหมายเปิด-ปิดตรงกันทั้งหมด
    return stack.is_empty()

# รับ JSON string จากผู้ใช้
json_string = input("กรุณากรอก JSON string: ")

# ตรวจสอบความถูกต้องของ JSON string
if is_valid_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
