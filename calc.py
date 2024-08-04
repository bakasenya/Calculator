import math

print("Welcome to the Calculator app!")
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

while True:
    try:
        x = float(input("Please enter the first number: "))
        y = float(input("Please enter the second number: "))

        break
    except ValueError:
        print("Please enter a valid number")




while True:
    user_choice = input("What operation do you want to perform?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Quit\nChoose - (1/2/3/4/5) or (Add/Sub/Mul/Div/Quit): ").lower()
    
    if user_choice == "1" or user_choice == "add":
        result = add(x, y)
        print(f"The result is {result}.")

    elif user_choice == "2" or user_choice == "sub":
        result = sub(x, y)
        print(f"The result is {result}")

    elif user_choice == "3" or user_choice == "mul":
        result = mul(x, y)
        print(f"The result is {result}")

    elif user_choice == "4" or user_choice == "div":
        result = div(x, y)
        print(f"The result is {result}")

    elif user_choice == "5" or user_choice == "quit":
        break
    else:
        print("Please enter a valid operation")
        continue

