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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_valid_json(json_string):
    """ตรวจสอบความถูกต้องของ JSON string"""
    stack = Stack()
    in_string = False  # ใช้ตรวจสอบว่าอยู่ในเครื่องหมาย "" หรือไม่

    for i, char in enumerate(json_string):
        if char == '"':
            # ถ้าพบ " ให้สลับสถานะ in_string (ไม่สนใจ "" ที่อยู่ใน string)
            if not stack.is_empty() and stack.peek() == '"':
                stack.pop()
            else:
                stack.push('"')

        if in_string:  # ถ้าอยู่ใน string ข้ามตัวอักษรอื่นไป
            continue

        if char in '{[':  # เปิดวงเล็บ
            stack.push(char)
        elif char in '}]':  # ปิดวงเล็บ
            if stack.is_empty():
                return False  # ไม่มีตัวเปิดที่ตรงกัน
            top = stack.pop()
            if (char == '}' and top != '{') or (char == ']' and top != '['):
                return False

    # ตรวจสอบว่ามีวงเล็บเปิดที่ยังไม่ได้ปิด
    if not stack.is_empty():
        return False

    # ตรวจสอบการพยายามใช้ JSON string แบบพื้นฐานด้วย eval
    try:
        import json
        json.loads(json_string)
    except (json.JSONDecodeError, ValueError):
        return False

    return True


# รับ JSON string จากผู้ใช้
json_string = input("กรุณาป้อน JSON string: ")

# ตรวจสอบความถูกต้อง
if is_valid_json(json_string):
    print(f"JSON string '{json_string}' ถูกต้อง")
else:
    print(f"JSON string '{json_string}' ไม่ถูกต้อง")
