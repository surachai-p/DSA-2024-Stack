### 1.โปรแกรมกลับลำดับตัวอักษร
  #จงเขียนโปรแกรมกลับลำดับตัวอักษรในข้อความโดยใช้ Stack (รับข้อความมาจากผู้ใช้งาน)

def reverse_string(s):

  stack = []
  for char in s:
    stack.append(char)

  reversed_string = ""
  while stack:
    reversed_string += stack.pop()
  return reversed_string

if __name__ == "__main__":
  input_string = input("กรุณาป้อนข้อความ: ")
  result = reverse_string(input_string)
  print("ข้อความที่กลับลำดับแล้ว:", result)