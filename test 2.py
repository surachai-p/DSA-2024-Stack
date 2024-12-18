class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def decimal_to_binary(num):
    s = Stack()

    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    binary_str = ""
    while not s.is_empty():
        binary_str += str(s.pop())

    return binary_str

def decimal_to_hexadecimal(num):
    s = Stack()
    hex_digits = "0123456789ABCDEF"

    while num > 0:
        remainder = num % 16
        s.push(hex_digits[remainder])
        num = num // 16

    hex_str = ""
    while not s.is_empty():
        hex_str += s.pop()

    return hex_str

# รับ input จากผู้ใช้
decimal_num = int(input("ป้อนเลขฐาน 10: "))

# แปลงและแสดงผลลัพธ์
binary_result = decimal_to_binary(decimal_num)
hexadecimal_result = decimal_to_hexadecimal(decimal_num)

print("เลขฐาน 2: ", binary_result)
print("เลขฐาน 16: ", hexadecimal_result)