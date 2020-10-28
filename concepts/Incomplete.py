num1 = input()
num2 = input()
op = input()

if num2 == 0.0 and op in ["mod", "div", "/"]:
    print("Division by 0!")
elif op == "+":
    print(float(num1) + float(num2))
elif op == "-":
    print(float(num1) - float(num2))
elif op == "*":
    print(float(num1) * float(num2))
elif op == "mod":
    print(int(num1) % int(num2))
elif op == "pow":
    print(float(num1) * float(num2))
elif op == "div":
    print(float(num1) // float(num2))
elif op == "/":
    print(float(num1) / float(num2))
