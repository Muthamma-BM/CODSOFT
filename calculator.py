print("welcome to the python calculator!")
try:
    num1=float(input("enter the first number: "))
    operator=input("enter operation(+,-,/,*) ")
    num2=float(input("enter the second number: "))
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 != 0:
            result = num1/num2
        else:
            print("Error: cannot divide by zero.")
            exit()
    else:
        print("invalid operation.")
        exit()
    print(f"Result: {num1} {operator} {num2} = {result}")
except ValueError:
    print("invalid input.Please enter numeric values.")                                