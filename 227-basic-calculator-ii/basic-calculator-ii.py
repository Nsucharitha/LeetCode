class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')  # remove spaces
        stack = []
        num = 0
        op = '+'  # default operator is '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            # If we hit an operator or end of string, apply previous operator
            if char in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))  # truncate toward zero

                op = char
                num = 0

        return sum(stack)