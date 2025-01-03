# Calculator in python

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("num1: "))
num2 = float(input("num2: "))

if operator == "+":
    res = num1 + num2
elif operator == "-":
    res = num1 - num2
elif operator == "*":
    res = num1 * num2
elif operator == "/":
    res = num1 / num2

print(res)