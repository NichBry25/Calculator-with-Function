# def make_shirt(size, message):
#     print(f"I made a shirt!")
#     print(f"The size of my shirt is {size}, with a message on it which is {message}.")
# make_shirt(message="Dog", size="20")

# messages = ["Gyattzers", "Skibidi"]
# def show_message(message):
#     for sentence in message:
#         print(sentence)
# show_message(messages)

# import math
# from math import sqrt
# from math import sqrt as root
# from math import *
# print(root(64))

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