number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
op = input("Enter an operator (+, -, *, /, **): ")

def calculator(num1, num2, operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2
    elif operator=="**":
        return num1**num2
    
print(calculator(number1, number2, op))
