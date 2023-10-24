import math

op =input("Enter op(+,-,*,/,sin,cos,cot,tan,sqrt,factorial):")

A = float(input("Enter your num A:"))
B = float(input("Enter your num B:"))
x = float(input("Enter num x:"))

if op == "+":
    print(A+B)
if op == "-":
    print(A-B)
if op == "*":
    print(A*B)
if op == "/":
    if B == 0:
        print("Nadarim")
else:
    print(A/B)

if op == "sin":
    print(math.sin(math.radians(x)))
if op == "cos":
    print(math.cos(math.radians(x)))
if op == "cot":
    print(math.cot(math.radians(x)))
if op == "tan":
    print(math.tan(math.radians(x)))
if op == "sqrt":
    print(math.sqrt(math.radians(x)))
if op == "factorial":
    print(math.factorial(math.radians(x)))