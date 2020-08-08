num1 = int(input("Enter your first number: "))
operator = input("Enter your operator:")
num2 = int(input("Enter your  second number: "))

if num1 == 45 and num2 == 3 and operator == "*":
    print(555)
elif num1 == 56 and num2 == 9 and operator == "+":
    print(77)
elif num1 == 56 and num2 == 6 and operator == "/":
    print(4)
elif operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)
else:
    print("Error!")
