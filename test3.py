#### 3: การคำนวณ Postfix Expression
   #จงเขียนฟังก์ชันสำหรับคำนวณผลลัพธ์ของนิพจน์ในรูปแบบ Postfix และทดสอบเรียกใช้งานโดยให้ผู้ใช้ป้อน Postfix Expression
def evaluate_postfix(expression):

    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2
            else:
                return "Invalid operator"
            stack.append(result)
    return stack.pop()

if __name__ == "__main__":
    postfix_expr = input("ป้อนนิพจน์ Postfix: ")
    result = evaluate_postfix(postfix_expr)
    print("ผลลัพธ์:", result)