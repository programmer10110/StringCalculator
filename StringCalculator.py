#simple stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, a):
        self.stack.append(a)
    def peek(self):
        if len(self.stack) > 0: return self.stack[len(self.stack)-1]
        else: return ""
    def pop(self):
        if len(self.stack) > 0: del self.stack[len(self.stack)-1]
        else: pass
    def getall(self):
        self.stack.reverse()
        return " ".join(self.stack)

#Reverse Polish Notation
def RPN(string):
    finish_string = ""
    stack = Stack()
    operations = "+-/*^"
    priority = {"(":1, "+":2, "-":2, "*":3, "/":3, "^":4, "":0} #operator precedence
    number = "" #helps to extract numbers
    index = 0   #helps to extract numbers
    for symbol in string:
        if symbol.isdigit():
            number += symbol
            if index == len(string)-1:
                finish_string += number
        elif symbol == "(":
            stack.push("(")
        elif symbol == ")":
            finish_string = finish_string + number + " "
            number = ""
            while stack.peek() != "(":
                finish_string = finish_string + stack.peek()
                stack.pop()
            if stack.peek() == "(":
                stack.pop()
        elif symbol in operations:
            finish_string = finish_string + number + " "
            number = ""
            while priority[symbol] <= priority[stack.peek()]:
                if priority[symbol] >= priority[stack.peek()]:
                    finish_string = finish_string + " " + stack.peek() + " "
                    stack.pop()
            stack.push(symbol)
        index += 1
    return (finish_string + " " + stack.getall()).strip()

def eval(string):
    operations = "+-*/^"
    rpn_string = RPN(string).split()
    stack = Stack()
    for i in rpn_string:
        if i.isdigit():
            stack.push(i)
        elif i in operations:
            if i == "+":
                a = stack.peek()
                stack.pop()
                b = stack.peek()
                stack.pop()
                stack.push(int(a) + int(b))
            elif i == "-":
                a = stack.peek()
                stack.pop()
                b = stack.peek()
                stack.pop()
                stack.push(int(b) - int(a))
            elif i == "*":
                a = stack.peek()
                stack.pop()
                b = stack.peek()
                stack.pop()
                stack.push(int(b) * int(a))
            elif i == "/":
                a = stack.peek()
                stack.pop()
                b = stack.peek()
                stack.pop()
                stack.push(int(b) / int(a))
            elif i == "^":
                a = stack.peek()
                stack.pop()
                b = stack.peek()
                stack.pop()
                stack.push(int(b) ** int(a))
        else:
            pass
    return stack.peek()