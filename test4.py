#### 4: การตรวจสอบ JSON string
   #จงเขียนโปรแกรมตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack และทดสอบเรียกใช้งานโดยให้ผู้ใช้งานป้อน JSON string

def is_valid_json(json_string):
    stack = []
    opening_brackets = '{'
    closing_brackets = '}'
    opening_brackets += '['
    closing_brackets += ']'
    brackets_map = {opening_brackets[i]: closing_brackets[i] for i in range(len(opening_brackets))}

    for char in json_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or char != brackets_map[stack.pop()]:
                return False
    return not stack

if __name__ == "__main__":
    json_str = input("ป้อน JSON string: ")
    if is_valid_json(json_str):
        print("JSON string ถูกต้อง")
    else:
        print("JSON string ไม่ถูกต้อง")