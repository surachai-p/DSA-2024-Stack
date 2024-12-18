def reverse_string_using_stack(string):
    """
    ฟังก์ชันกลับลำดับตัวอักษรในข้อความโดยใช้ Stack

    Args:
        string: ข้อความที่จะกลับลำดับ

    Returns:
        str: ข้อความที่กลับลำดับแล้ว
    """

    stack = []
    for char in string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

if __name__ == "__main__":
    input_string = input("กรุณาป้อนข้อความ:  ")
    result = reverse_string_using_stack(input_string)
    print("ข้อความที่กลับลำดับแล้ว:", result)