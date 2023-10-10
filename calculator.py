print('Welcome to a calculator application. Here you can do a simple math with two numbers!')
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
sign = input("""Please enter a sign of the opperation you want to make between these two numbers. 
Please note, that valid operations are: +, -, *, /, %, ^: """)
result = 0
if sign == "+":
    result = x+y
elif sign == "-":
    result = x-y
elif sign == "*":
    result = x*y
elif sign == "/":
     if y !=0:
        result = float(x/y)
     else:
        print("Cannot divide by zero")
        exit()
elif sign == "%":
     if y !=0:
        result = x%y
     else:
        print("Cannot divide by zero")
        exit()
elif sign == "^":
    result = x**y
else:
    print(f"The operation you have provided cannot be done. We are not supporting the sign: {sign}")
    exit()
print("The answer of this calculation is: ", result)