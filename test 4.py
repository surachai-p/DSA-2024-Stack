def is_valid_json(json_string):
    """
    ตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack

    Args:
        json_string (str): JSON string ที่ต้องการตรวจสอบ

    Returns:
        bool: True ถ้า JSON string ถูกต้อง False ถ้าไม่ถูกต้อง
    """

    stack = []
    opening_brackets = ['{', '[']
    closing_brackets = ['}', ']']
    
    for char in json_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    
    return not stack

# รับ input จากผู้ใช้
json_string = input("กรุณาป้อน JSON string: ")

# ตรวจสอบและแสดงผลลัพธ์
if is_valid_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")