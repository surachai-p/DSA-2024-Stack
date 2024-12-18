def is_valid_json(json_string):
    # Stack สำหรับเก็บวงเล็บเปิด
    stack = []

    # คู่ของวงเล็บที่ถูกต้อง
    matching_brackets = {
        '}': '{',
        ']': '['
    }

    # วนลูปผ่านทุกตัวอักษรใน JSON string
    for char in json_string:
        # ถ้าเป็นวงเล็บเปิด ให้ใส่ลงใน Stack
        if char in '{[':
            stack.append(char)
        
        # ถ้าเป็นวงเล็บปิด ให้ตรวจสอบว่าตรงกับวงเล็บเปิดใน Stack หรือไม่
        elif char in '}]':
            # ถ้า Stack ว่างหรือวงเล็บไม่จับคู่กัน
            if not stack or stack.pop() != matching_brackets[char]:
                return False

    # ถ้า Stack ว่างหลังจากตรวจสอบทั้งหมด แสดงว่าถูกต้อง
    return len(stack) == 0


# รับ JSON string จากผู้ใช้งาน
user_input = input("กรอก JSON string ที่ต้องการตรวจสอบ: ")

# เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
if is_valid_json(user_input):
    print("JSON string นี้ถูกต้อง (วงเล็บจับคู่กันถูกต้อง)")
else:
    print("JSON string นี้ไม่ถูกต้อง (วงเล็บไม่สมดุลหรือไม่จับคู่)")
