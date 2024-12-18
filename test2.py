### 2.โปรแกรมแปลงเลขฐาน
   #จงเขียนโปรแกรมแปลงเลขฐาน 10 ให้เป็นฐาน 2 และ ฐาน 16 โดยใช้ Stack และทดสอบเรียกใช้งานโดยรับตัวเลขฐาน 10 มาจากผู้ใช้งาน
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

def decimal_to_binary(num):
    stack = Stack()
    while num > 0:
        remainder = num % 2
        stack.push(remainder)
        num //= 2

    binary_str = ""
    while not stack.is_empty():
        binary_str += str(stack.pop())
    return binary_str

def decimal_to_hexadecimal(num):
    hex_digits = "0123456789ABCDEF"
    stack = Stack()
    while num > 0:
        remainder = num % 16
        stack.push(hex_digits[remainder])
        num //= 16

    hex_str = ""
    while not stack.is_empty():
        hex_str += stack.pop()
    return hex_str

if __name__ == "__main__":
    decimal_num = int(input("ป้อนเลขฐาน 10: "))
    binary_result = decimal_to_binary(decimal_num)
    hexadecimal_result = decimal_to_hexadecimal(decimal_num)

    print(f"เลขฐาน 2: {binary_result}")
    print(f"เลขฐาน 16: {hexadecimal_result}")