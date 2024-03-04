try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = a + b
except SyntaxError as s:
    print("Syntax Error:", s)
else:
    print("Sum:", c)
